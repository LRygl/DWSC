from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait


from scraperUtils.dateUtils import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import time
    from dataWriter import writeDataToCsv

    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    # Path to chromedriver executable
    driver_path = 'C:/WebDriver/chromedriver.exe'

    # Create ChromeOptions instance
    chrome_options = Options()

    # Add any desired options
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
    chrome_options.add_argument('--disable-logging') #Disables logging of the Chrome driver (saves memory)
    chrome_options.add_argument('--disable-notifications') #Disables browser notifications.

    # Open the URL
    #url = 'https://www.sazka.cz/kurzove-sazky/'
    #url = 'https://www.sazka.cz/kurzove-sazky/sports/competition/1125/fotbal/cesko/cesko-1liga/matches'

    # List of tuples containing pairs (Category, League, URL) - add more as needed
    category_url_pairs = [
        ('Fotbal', "Česko 1.liga", 'https://www.sazka.cz/kurzove-sazky/sports/competition/1125/fotbal/cesko/cesko-1liga/matches'),
        ('Hokej', "Česko 1.liga", 'https://www.sazka.cz/kurzove-sazky/sports/competition/3013/hokej/cesko/cesko-1liga/matches'),
        # Add more pairs as needed
    ]



    # Go trough the URLs in category_url_pairs and scrape data
    for category, league, url in category_url_pairs:
        run_start_time = getTime()

        # Create a Chrome WebDriver instance with options
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(3)  # Let the user actually see something!

        elements = driver.find_elements(By.TAG_NAME, 'li')
        # TODO GET ADDITIONAL ELEMENTS FOR GIVEN MATCH - EXTRACT TO A SEPARATE METHOD

       # Get the list of teams
        partial_team_class_name = "eventCardTeamName-0-3-"  # Replace with your desired partial class name
        team_pairs = driver.find_elements(By.CSS_SELECTOR, f'div[class^="{partial_team_class_name}"]')
        print("TEAMS")

        teams = []

        # Loop through the matching elements
        counter = 1
        for element in team_pairs:
            # Perform actions on the matched elements

            if counter%2 == 0:
                print("Team B:" + element.text.strip())
                teams.append(element.text.strip())
            else:
                print("Team A:" + element.text.strip())
                teams.append(element.text.strip())
            counter=counter+1






        #
        partial_class_name = "outcomePriceCommon-0-3-"  # Replace with your desired partial class name
        values = driver.find_elements(By.CSS_SELECTOR, f'span[class^="{partial_class_name}"]')
        print("Vítěz a góly nad/pod")

        # Loop through the matching elements
        for value in values:
            # Perform actions on the matched elements
            print(value.text.strip())  # Extract and print the text content of each li element






        # Print the data to the csv file and format them
        print(f"Category: {category}")
        print(f"League: {league}\n")
        print(f"URL: {url}\n")
        writeDataToCsv(elements, category, league, teams)
        driver.quit()

        run_end_time = getTime()
        time_elapsed = run_end_time - run_start_time
        print(f"Elapsed Time: {time_elapsed:.6f} seconds")
