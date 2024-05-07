from robocorp.tasks import task
from robocorp import browser

from RPA.HTTP import HTTP
from RPA.Excel.Files import Files
from RPA.PDF import PDF


@task
def robot_spare_bin_python():
    """Insert the sales data for the weel and export it as a PDF"""
    browser.configure(
        slowmo=100,
    )
    open_the_intranet_website()
    log_in()
    download_excel_file()
    validate_data()
    fill_form_with_excel_file()
    collect_results()
    export_as_pdf()
    log_out()


def open_the_intranet_website():
    """Navigate to the given URL"""
    browser.goto("https://robotsparebinindustries.com/")


def log_in():
    """Fills the login form and clicks the 'Log in' button"""
    page = browser.page()
    page.fill("#username", "maria")
    page.fill("#password", "thoushallnotpass")
    page.click("button:text('Log in')")


def download_excel_file():
    """Downloads the excel file from the given URL"""
    http = HTTP()
    http.download(url="https://robotsparebinindustries.com/SalesData.xlsx", overwrite=True)


def validate_data():
    """Validate the data from the excel file"""
    


def fill_form_with_excel_file():
    """Fills in the sales data and click the 'Submit' button"""
    pass


def collect_results():
    """Take a screenshot of the page"""
    pass


def export_as_pdf():
    """Export the data to a pdf file"""
    pass


def log_out():
    """Pressures the 'Log out' button"""
    pass

