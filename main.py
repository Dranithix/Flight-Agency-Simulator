#-------------------------------------------------------------------------------
# Name:        DSCTravelAgency
# Purpose:     Allows clients of a travel agency to book a flight.
#
# Author:      Kenta Iwasaki
#
# Created:     29/05/2014
# Copyright:   (c) Kenta Iwasaki 2014
# Licence:     N/A
#-------------------------------------------------------------------------------

# Internal Python Module Imports
import sys, random, urllib.request, json, sqlite3, os, bs4, re

# PyQT Framework Module Imports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtWebKitWidgets import *

# PyQT Generated UI Module Imports
from ui_login import Ui_LoginDialog
from ui_register import Ui_RegisterDialog
from ui_main import Ui_MainWindow
from ui_airport import Ui_AirportDialog
from ui_order import Ui_OrderDialog
from ui_flight import Ui_FlightDialog
from ui_progress import Ui_ProgressDialog
from ui_manager import Ui_ManagerDialog

# Client Account Status
CLIENT_ACCOUNT = 0
MANAGER_ACCOUNT = 1

# Holds flight results from online sources.
flightResults = []

# Holds recently booked flights by the client.
recentFlights = []

# Unitialized null variables.
app = None
db = None

currentAccount = None
fromDestination = None
toDestination = None
currentFlight = None

mainWindow = None
loginDialog = None
registerDialog = None
airportDialog = None
orderDialog = None
flightDialog = None
progressDialog = None
managerDialog = None

# Represents an client's account.
class Account:
    def __init__(self, username, password, status, name, dob, points):
        self.username = username
        self.password = password
        self.status = int(status)
        self.name = name
        self.dob = dob
        self.points = points

# Represents a booked flight by a client.
class Order:
    def __init__(self, username, ticket, cctype, ccnum, cvc, name, address, phone, airline, price, form, departTakeoff, departLanding, returnTakeoff, returnLanding, date, fromDestination, toDestination, layover):
        self.username = username
        self.ticket= ticket
        self.cctype = cctype
        self.ccnum = ccnum
        self.cvc = cvc
        self.name = name
        self.address = address
        self.phone = phone
        self.airline = airline
        self.price = price
        self.form = form
        self.departTakeoff = departTakeoff
        self.departLanding = departLanding
        self.returnTakeoff = returnTakeoff
        self.returnLanding = returnLanding
        self.date = date
        self.fromDestination = fromDestination
        self.toDestination = toDestination
        self.layover = layover

# Represents a single flight search result.
class Flight:
    def __init__(self, airlineName, price, departDuration, departTakeoff, departArrive, returnDuration, returnTakeoff, returnArrive, layover):
        self.airlineName = airlineName
        self.price = float(price.replace("$", ""))
        # Determines the class of a flight by randomization. Sets price according to value of class as well.
        classType = random.randint(0, 3)
        if (classType == 0):
            self.form = "Economy"
        elif (classType == 1):
            self.form = "Premium Economy"
            self.price *= 1.1
        elif (classType == 2):
            self.form = "Business"
            self.price *= 1.3
        else:
            self.form = "First"
            self.price *= 1.5
        self.departDuration = departDuration
        self.departTakeoff = departTakeoff
        self.departArrive = departArrive
        self.returnDuration = returnDuration
        self.returnTakeoff = returnTakeoff
        self.returnArrive = returnArrive
        self.layover = layover

# Represents an airport, along with its IATA ID.
class Airport:
    def __init__(self, name, iata):
        self.name = name
        self.iata = iata

# Represents the login window of the application.
class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.setupUi(self)

        # Sets event handlers for components of the UI.
        self.btnLogin.clicked.connect(self.login)
        self.btnRegister.clicked.connect(self.register)

    # Logs the user in and retrieves their account information from a SQLite Database.
    def login(self):
        global db, currentAccount

        loginQuery = db.execute("SELECT * FROM accounts WHERE username = ? AND password = ?", (self.txtUser.text().strip(), self.txtPass.text().strip()))
        loginResult = loginQuery.fetchone()
        # Error handles if the account could be found in the database or not.
        if (loginResult == None):
            QMessageBox.information(self, "Login", "We could not find your account in our database.")
        else:
            currentAccount = Account(loginResult[0], loginResult[1], loginResult[2], loginResult[3], loginResult[4], int(loginResult[5]))
            QMessageBox.information(self, "Login", "Welcome to DSC, %s!" % (currentAccount.name))
            self.hide()
            mainWindow.idLabel.setText(currentAccount.username)
            mainWindow.nameLabel.setText(currentAccount.name)
            mainWindow.dobLabel.setText(currentAccount.dob)
            mainWindow.pointsLabel.setText(str(currentAccount.points))
            mainWindow.updateRecentFlights()
            mainWindow.btnManager.setVisible(currentAccount.status == MANAGER_ACCOUNT)
            mainWindow.show()

    # Opens the registration window.
    def register(self):
        registerDialog.exec_()

# Represents the airport search dialog of the program.
class AirportDialog(QDialog, Ui_AirportDialog):
    def __init__(self, destination):
        super(AirportDialog, self).__init__()
        self.setupUi(self)
        self.destination = destination
        self.airports = []

        # Sets event handlers for components of the UI.
        self.btnSearch.clicked.connect(self.searchAirport)
        self.btnSelectAirport.clicked.connect(self.selectAirport)

    # Searches Word-Airport-Codes.com for airport IATA's and information requested by the client.
    def searchAirport(self):
        self.airportList.clear()
        # Masks user-agent of the HTTP GET request sent to the airport database.
        request = urllib.request.Request("http://www.world-airport-codes.com/search/?s=" + self.txtAirport.text().strip().replace(" ", "+"), headers = {'User-Agent' : 'Mozilla/5.0'})
        soup = bs4.BeautifulSoup(urllib.request.urlopen(request).read())
        routeTable = soup.findChildren("table")
        if (len(routeTable) <= 0): # Provides an error if the airport could not be found in the database.
            QMessageBox.information(self, "Airport Search", ("\"%s\" could not be found." % (self.txtAirport.text().strip())))
        else:
            # Provides found airports into a GUI List if an airport's name matching a search term was found.
            rows = routeTable[0].findChildren(['th', 'tr'])
            for row in rows:
                cells = row.findChildren(['a', 'td'])
                if (len(cells) >= 2):
                    if (cells[2].string is not None and cells[1].string is not None):
                        self.airports.append(Airport(cells[0].string.strip(), cells[1].string.strip()))
                        QListWidgetItem(cells[0].string.strip(), self.airportList)

    # Sets the airport information into the designated To/From fields of the program.
    def selectAirport(self):
        global fromDestination, toDestination
        selected = self.airportList.currentItem()
        if (selected is not None): # Determines if the client has selected an airport from a list of found airports.
            if (self.destination): # Determines if the invoked airport search is for the From/Destination Fields of the program.
                for airport in self.airports:
                    if (airport.name == selected.text()):
                        toDestination = airport
                mainWindow.txtDestination.setText(selected.text())
            else:
                for airport in self.airports:
                    if (airport.name == selected.text()):
                        fromDestination = airport
                mainWindow.txtFrom.setText(selected.text())
            # Hides and clears the airport search results.
            self.hide()
            self.airportList.clear()
        else:
            QMessageBox.information(self, "Airport Search", "You have not selected any airport.")

# Represents the registration window of the program for registration of accounts..
class RegisterDialog(QDialog, Ui_RegisterDialog):
    def __init__(self):
        super(RegisterDialog, self).__init__()
        self.setupUi(self)

        # Sets event handlers for components of the UI.
        self.btnRegister.clicked.connect(self.register)
        self.txtDate.setDateTime(QDateTime.currentDateTime().addYears(-18))

    # Register's an users account and inserts their account into the database.
    def register(self):
        global db
        if (not self.txtName.text() or not self.txtPass.text()):
            QMessageBox.information(self, "Register", "You have not filled in one or more fields.")
        else:
            userId = str(random.randint(10**(5-1), 10**5-1)) # Creates a randomized User ID 5 digits in length.
            db.execute("INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?)", (userId, self.txtPass.text().strip(), CLIENT_ACCOUNT, self.txtName.text().strip(), self.txtDate.date().toPyDate(), 0))
            db.commit()

            # Sets the randomized User ID to their clipboard.
            os.system("echo " + userId.strip() + "| clip")
            # Clears the fields of the registration window and hides the window.
            self.txtName.setText("")
            self.txtPass.setText("")
            self.hide()
            QMessageBox.information(self, "Register", "Your account has been registered! Your new User ID is copied into your clipboard. User ID: " + userId)

# Represents the flight booking order window of the program.
class OrderDialog(QDialog, Ui_OrderDialog):
    def __init__(self):
        super(OrderDialog, self).__init__()
        self.setupUi(self)

        # Sets event handlers for components of the UI.
        self.pushButton.clicked.connect(self.orderConfirm)

    # Inserts the booked flight into the database after asking for order confirmation.
    def orderConfirm(self):
        global mainWindow
        reply = QMessageBox.question(self, "Order Confirmation", "Are you sure you would like to book this flight?")
        if (reply == QMessageBox.Yes): # Determines if the client proceeds with filing the booking.
            if (not self.txtCcNumber.text() or not self.lineEdit.text() or not self.txtBillingName.text() or not self.txtBillingAddress.text() or not self.txtPhone.text()): # Determines if all fields of the order process are filled.
                QMessageBox.information(self, "Order Confirmation", "One or more of the fields are not filled in.")
            else:
                currentAccount.points += int(float(self.txtPrice.text().strip().replace("$", "")) * 0.2) # Increment amount of flyer points on account.
                ticketId = str(random.randint(10**(15-1), 10**15-1)) # Creates a randomized flight ticket ID 10 letters long.

                # Update orders and accounts within the database.
                db.execute("INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (currentAccount.username, ticketId, self.txtCcType.currentText().strip(), self.txtCcNumber.text().strip(), self.lineEdit.text().strip(), self.txtBillingName.text().strip(), self.txtBillingAddress.text().strip(), self.txtPhone.text().strip(), self.txtAirline.text().strip(), self.txtPrice.text().strip().replace("$", ""), self.txtClass.text().strip(), self.txtDepartTakeoff.text().strip(), self.txtDepartLanding.text().strip(), self.txtReturnTakeoff.text().strip(), self.txtReturnLanding.text().strip(), QDateTime.currentDateTime().date().toPyDate(), mainWindow.txtFrom.text().strip(), mainWindow.txtDestination.text().strip(), self.txtLayover.text().strip()))
                db.execute("UPDATE accounts SET points = ? WHERE username = ?", (str(currentAccount.points), currentAccount.username))
                db.commit() # Inserts the booked flight into the database.
                mainWindow.updateRecentFlights()
                mainWindow.pointsLabel.setText(str(currentAccount.points))
                QMessageBox.information(self, "Order Confirmation", "Your order has been confirmed and processed. Check your recent transactions for order information.")
                self.hide()

# Represents the flight summary window of the program.
class FlightDialog(QDialog, Ui_FlightDialog):
    def __init__(self):
        super(FlightDialog, self).__init__()
        self.setupUi(self)

# Represents the manager panel of the program.
class ManagerDialog(QDialog, Ui_ManagerDialog):
    def __init__(self):
        super(ManagerDialog, self).__init__()
        self.setupUi(self)

    # Loads financial statistics from the entire database; includes income, commission, and all transactions.
    def loadStatistics(self):
        totalIncome = 0.0
        flightsQuery = db.execute("SELECT * FROM orders")
        allFlights = flightsQuery.fetchall() # Queries for all booked flights in the datbaase.
        self.transactions.setRowCount(len(allFlights))

        # Place all transaction data within respective tables.
        for index, row in enumerate(allFlights):
            totalIncome += float(row[9])
            userObj = QTableWidgetItem(row[0])
            dateObj = QTableWidgetItem(row[15])
            priceObj = QTableWidgetItem(row[9])
            airlineObj = QTableWidgetItem(row[8])
            ticketObj = QTableWidgetItem(row[1])
            nameObj = QTableWidgetItem(row[5])
            addressObj = QTableWidgetItem(row[6])
            phoneObj = QTableWidgetItem(row[7])

            userObj.setFlags(Qt.ItemIsEnabled)
            dateObj.setFlags(Qt.ItemIsEnabled)
            priceObj.setFlags(Qt.ItemIsEnabled)
            airlineObj.setFlags(Qt.ItemIsEnabled)
            ticketObj.setFlags(Qt.ItemIsEnabled)
            nameObj.setFlags(Qt.ItemIsEnabled)
            addressObj.setFlags(Qt.ItemIsEnabled)
            phoneObj.setFlags(Qt.ItemIsEnabled)

            self.transactions.setItem(index, 0, userObj)
            self.transactions.setItem(index, 1, dateObj)
            self.transactions.setItem(index, 2, priceObj)
            self.transactions.setItem(index, 3, airlineObj)
            self.transactions.setItem(index, 4, ticketObj)
            self.transactions.setItem(index, 5, nameObj)
            self.transactions.setItem(index, 6, addressObj)
            self.transactions.setItem(index, 7, phoneObj)
        self.transactions.verticalHeader().setVisible(False)

        # Calculates and sets the labels for all financial statistics.
        self.txtIncome.setText("$%.2f" % (totalIncome))
        self.txtCommission.setText("$%.2f" % (totalIncome * 0.2))
        self.txtFinalIncome.setText("$%.2f" % (totalIncome - (totalIncome * 0.2)))

# Represents a loading progress dialog of the program.
class ProgressDialog(QDialog, Ui_ProgressDialog):
    def __init__(self):
        super(ProgressDialog, self).__init__()
        self.setupUi(self)

    # Sets the progress bar percentage of the dialog.
    def setProgress(self, num):
        self.progressBar.setValue(num)

# Represents the main window of the program.
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Sets event handlers for components of the UI.
        self.btnAirportSearch.clicked.connect(self.searchAirport)
        self.btnAirportSearch_2.clicked.connect(self.searchAirport2)
        self.btnSearchFlight.clicked.connect(self.searchFlight)
        self.btnBookFlight.clicked.connect(self.bookFlight)
        self.btnManager.clicked.connect(self.openManagerPanel)
        self.recentFlightsTable.cellDoubleClicked.connect(self.loadFlightSummary)

        # Sets the date fields of the GUI to the current date & time. Also sets restrictions on the date fields for error handling.
        self.departureDate.setDateTime(QDateTime.currentDateTime())
        self.returnDate.setDateTime(QDateTime.currentDateTime().addDays(7))
        self.departureDate.setMinimumDateTime(QDateTime.currentDateTime())
        self.returnDate.setMinimumDateTime(QDateTime.currentDateTime().addDays(1))

        # Sets up a web page interpreter, and connects event handlers to the program for interpreting HTTP Data.
        self.webPage = QWebPage()
        self.webPage.loadFinished.connect(self.getSource)
        self.webPage.loadProgress.connect(self.updateProgress)

    # Opens up the manager panel.
    def openManagerPanel(self):
        managerDialog.loadStatistics()
        managerDialog.exec_()

    # Sets the progress bar value.
    def updateProgress(self, progress):
        progressDialog.setProgress(progress)

    # Sets the variables of the flight summary window according to selected rows and opens it.
    def loadFlightSummary(self, row, column):
        global recentFlights
        summary = recentFlights[row]
        flightDialog.txtAirline.setText(summary.airline)
        flightDialog.txtPrice.setText("$%.2f" % (float(summary.price)))
        flightDialog.txtClass.setText(summary.form)
        flightDialog.txtDepartTakeoff.setText(summary.departTakeoff)
        flightDialog.txtDepartLanding.setText(summary.departLanding)
        flightDialog.txtReturnTakeoff.setText(summary.returnTakeoff)
        flightDialog.txtReturnLanding.setText(summary.returnLanding)
        flightDialog.txtTicket.setText(summary.ticket)
        flightDialog.txtDate.setText(summary.date)
        flightDialog.txtCcType.setText(summary.cctype)
        flightDialog.txtBillingName.setText(summary.name)
        flightDialog.txtBillingAddress.setText(summary.address)
        flightDialog.txtPhone.setText(summary.phone)
        flightDialog.txtFrom.setText(summary.fromDestination)
        flightDialog.txtTo.setText(summary.toDestination)
        flightDialog.txtLayover.setText(summary.layover)
        flightDialog.exec_()

    # Clears out all recent flight data held in the program, and queries the SQLite database for the data again.
    def updateRecentFlights(self):
        global recentFlights, db, currentAccount
        del recentFlights[:] # Clears all recent flights data stored in the program.
        flightsQuery = db.execute("SELECT * FROM orders WHERE username = ?", (currentAccount.username,))
        for row in flightsQuery.fetchall(): # Fetches all results from the query.
            recentFlights.append(Order(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18]))
        # Clears recent flights table contents and re-populates the entries.
        self.recentFlightsTable.clearContents()
        self.recentFlightsTable.setRowCount(len(recentFlights))
        for index, flight in enumerate(recentFlights):
            flightObj = QTableWidgetItem(flight.date + " " + flight.airline)
            flightObj.setFlags(Qt.ItemIsEnabled)
            self.recentFlightsTable.setItem(index, 0, flightObj)
        self.recentFlightsTable.setColumnWidth(0, 180)
        self.recentFlightsTable.verticalHeader().setVisible(False)

    # Opens the airport search dialog.
    def searchAirport(self):
        airportDialog = AirportDialog(False)
        airportDialog.exec_()

    # Opens the airport search dialog.
    def searchAirport2(self):
        airportDialog = AirportDialog(True)
        airportDialog.exec_()

    # Sends a HTTP GET Request to Kayak for a list of available flights according to the client.
    def searchFlight(self):
        global flightResults
        if (fromDestination is None or toDestination is None): # Determines if the user has selected a proper set of destinations for the flight.
            QMessageBox.information(self, "Search Flights", "You have not selected a To/From Destination.")
        else:
            webUrl = "http://www.kayak.com/flights/%s-%s/%s/%s" % (fromDestination.iata, toDestination.iata, self.departureDate.date().toPyDate(), self.returnDate.date().toPyDate())
            self.webPage.mainFrame().load(QUrl(webUrl))
            self.flightsTable.clearContents()
            self.flightsTable.setRowCount(0)
            progressDialog.exec_() # Opens up a progress bar dialog to mark loading progress.
            del flightResults[:]

    # Returns a presently selected flight from a list of flight search results.
    def getCurrentFlight(self):
        try:
            return flightResults[self.flightsTable.currentRow()] if (self.flightsTable.currentRow() != -1) else None
        except:
            return None

    # Opens order confrimation dialog.
    def bookFlight(self):
        global currentFlight, currentAccount
        selectedFlight = self.getCurrentFlight()
        if (selectedFlight != None):
            currentFlight = selectedFlight
            orderDialog.txtAirline.setText(currentFlight.airlineName)
            orderDialog.txtPrice.setText("$%.2f" % (float(currentFlight.price)))
            orderDialog.txtClass.setText(currentFlight.form)
            orderDialog.txtBillingName.setText(currentAccount.name)
            orderDialog.txtDepartTakeoff.setText(currentFlight.departTakeoff)
            orderDialog.txtDepartLanding.setText(currentFlight.departArrive)
            orderDialog.txtReturnTakeoff.setText(currentFlight.returnTakeoff)
            orderDialog.txtReturnLanding.setText(currentFlight.returnArrive)
            orderDialog.txtLayover.setText(currentFlight.layover)
            orderDialog.exec_()
        else:
            QMessageBox.information(self, "Book Flights", "You have not selected a flight, or the selection you have chosen expired.")

    # Once a HTTP Request is returned from Kayak, its returned flight data is interpreted and populated into a search results table.
    def getSource(self, ok):
        global flightResults
        if (ok):
            # Uses BeautifulSoup in order to parse Kayak's web page data.
            soup = bs4.BeautifulSoup(self.webPage.mainFrame().toHtml())
            if (soup.find("div", {"class" : "noresults"}) is None):
                flightsTable = soup.find_all("div", {"class" : "airlineAndLegs"})
                flightPrices = soup.find_all("a", {"class" : "results_price"})
                for index, flight in enumerate(flightsTable):
                    layover = flight.find("div", {"class" : "stopsLayovers"}).string
                    flightResults.append(Flight(flight.find("div", {"class" : "airlineName"}).string.strip(), re.sub("\D", "", flightPrices[index].string.strip()), flight.find_all("div", {"class" : "duration"})[0].string.strip(), flight.find_all("div", {"class" : "flighttime flightTimeDeparture"})[0].string.strip(), flight.find_all("div", {"class" : "flighttime flightTimeArrival"})[0].string.strip(), flight.find_all("div", {"class" : "duration"})[1].string.strip(), flight.find_all("div", {"class" : "flighttime flightTimeDeparture"})[1].string.strip(), flight.find_all("div", {"class" : "flighttime flightTimeArrival"})[1].string.strip(), layover.strip() if layover != None else flight.find("div", {"class" : "stopsLayovers"}).find("span", {"class" : "airportslist"}).string.strip()))

                self.flightsTable.setRowCount(len(flightResults))
                for index, flight in enumerate(flightResults):
                    airlineObj = QTableWidgetItem(flight.airlineName)
                    priceObj = QTableWidgetItem("%.2f" % (flight.price))
                    classObj = QTableWidgetItem(flight.form)
                    departDurationObj = QTableWidgetItem(flight.departDuration)
                    departTakeoffObj = QTableWidgetItem(flight.departTakeoff)
                    departArriveObj = QTableWidgetItem(flight.departArrive)
                    returnDurationObj = QTableWidgetItem(flight.returnDuration)
                    returnTakeoffObj = QTableWidgetItem(flight.returnTakeoff)
                    returnArriveObj = QTableWidgetItem(flight.returnArrive)
                    layoverObj = QTableWidgetItem(flight.layover)

                    airlineObj.setFlags(Qt.ItemIsEnabled)
                    priceObj.setFlags(Qt.ItemIsEnabled)
                    classObj.setFlags(Qt.ItemIsEnabled)
                    departDurationObj.setFlags(Qt.ItemIsEnabled)
                    departTakeoffObj.setFlags(Qt.ItemIsEnabled)
                    departArriveObj.setFlags(Qt.ItemIsEnabled)
                    returnDurationObj.setFlags(Qt.ItemIsEnabled)
                    returnTakeoffObj.setFlags(Qt.ItemIsEnabled)
                    returnArriveObj.setFlags(Qt.ItemIsEnabled)
                    layoverObj.setFlags(Qt.ItemIsEnabled)

                    self.flightsTable.setItem(index, 0, airlineObj)
                    self.flightsTable.setItem(index, 1, priceObj)
                    self.flightsTable.setItem(index, 2, classObj)
                    self.flightsTable.setItem(index, 3, departDurationObj)
                    self.flightsTable.setItem(index, 4, departTakeoffObj)
                    self.flightsTable.setItem(index, 5, departArriveObj)
                    self.flightsTable.setItem(index, 6, returnDurationObj)
                    self.flightsTable.setItem(index, 7, returnTakeoffObj)
                    self.flightsTable.setItem(index, 8, returnArriveObj)
                    self.flightsTable.setItem(index, 9, layoverObj)

                self.flightsTable.verticalHeader().setVisible(False)
            else:
                QMessageBox.information(self, "Search Flights", "No flights could be found in your requested date range.")
            progressDialog.hide() # Hides the progress dialog once all data is finished loading.

# Loads the SQLite database and creates data tables for any client data accordingly.
def loadDatabase():
    global db
    db = sqlite3.connect("accounts.db")
    db.execute("CREATE TABLE IF NOT EXISTS accounts (username, password, status, name, dob, points)")
    db.execute("CREATE TABLE IF NOT EXISTS orders (username, ticket, cctype, ccnum, cvc, name, address, phone, airline, price, class, departTakeoff, departLanding, returnTakeoff, returnLanding, date, fromDestination, toDestination, layover)")
    db.commit()

# Closes the database connection on application exit.
def dispose():
    db.close()

# Creates a PyQT Application Context.
app = QApplication(sys.argv)
app.aboutToQuit.connect(dispose)

# Initializes all windows and dialogs for the program.
loginDialog = LoginDialog()
registerDialog = RegisterDialog()
orderDialog = OrderDialog()
flightDialog = FlightDialog()
progressDialog = ProgressDialog()
managerDialog = ManagerDialog()
mainWindow = MainWindow()
loginDialog.show()

# Loads the SQLite Database the program resolves around.
loadDatabase()

# Hooks an application exit call to the Python insterpreter.
sys.exit(app.exec_())