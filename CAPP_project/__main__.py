"""
Author: Eshan 
#Objective is to give user the flexibiity to jump to the app directly or just run sub-packages
"""
import sys
import pathlib
from CAPP_project.dash_app import app
from CAPP_project.data_wrangling import __main__ as dw_main
from CAPP_project.analysis_plots import __main__ as ap_main
from CAPP_project.raw_data.crime_api import crime_extract


def package_breakdown():
    """
    Function to run different files (and associated functions) based on input given by user in console
    Input: None
    Returns: None. Executes selected file/function and reports time to run
    """
    sys_args = ["fetch", "clean", "merge", "plot", "explore", "all"]
    print(f"Great! Choose one of the steps:{sys_args} or exit")
    arg = input().lower()
    if arg == "fetch":
        print(
            "Fetching crime data from Chicago data portal...this will take ~10 minutes! If you want to exit, press Ctrl+C"
        )
        crime_extract()
    if arg == "all":
        print(
            "This includes fetching latest data which takes ~10 mins; type y if you want to continue or type n if you want to skip fetching:[y/n]"
        )
        if input().lower() == "y":
            crime_extract()
            dw_main.run("clean")
            dw_main.run("merge")
            ap_main.run("plot")
            print("All grunt work done, ready to publish dash app!")
            app.run_server(port=6095)
        else:
            dw_main.run("clean")
            dw_main.run("merge")
            ap_main.run("plot")
            print("All grunt work done, ready to publish dash app!")
            app.run_server(port=6094)
    elif arg == "clean" or arg == "merge":
        dw_main.run(arg)
    elif arg == "plot":
        ap_main.run(arg)
    else:
        print(f"Unknown step: {arg}")
        sys.exit(1)


if __name__ == "__main__":
    print(
        "Hi user! Do you want to jump to our dash app or run the app stepwise? [jump/stepwise]"
    )
    arg = input().lower()
    if arg == "stepwise":
        package_breakdown()
    elif arg == "jump":
        app.run_server(port=6094)
        print("Now do you want to test step-wise operations? [y/n]")
        new_arg = input().lower()
        if new_arg == "y":
            package_breakdown()
        elif new_arg == "n":
            sys.exit(1)
        else:
            print(sys.argv)
            print(f"Unknown command:{new_arg}. Please try again!")
    else:
        print(f"Unknown command: {arg}")
        sys.exit(1)
