# Import libraries

from tkinter import *
from tkinter import ttk, font, messagebox, Toplevel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define unit-converter class

class UnitConverter:

    def __init__(self):
        #       Graphical Interface variables (settings)
        self.screen_size = '600x600'
        self.screen_size2 = '1200x600'
        self.font = 'Ubuntu Mono'
        self.background_color1 = 'NavajoWhite2'
        self.background_color2 = 'NavajoWhite3'
        self.element_color = 'NavajoWhite4'
        self.facecolor_plot = '#CAB48F'
        self.facecolor_plot2 = '#EDDDC2'
        self.plot_color = ['#0000FF', '#9932CC', '#FF69B4', '#A52A2A', '#FF8000', '#EEEE00', '#32CD32', '#40E0D0',
                           '#C0C0C0', '#98FB98', '#CD853F']
        self.plot_color2 = ['#E51D2E', '#497E76']

        #       Variables for factor. There are three types of unit converter:
        # ♣     Measure converter. There are length converter, weight converter, surface converter, volume converter, temperature converter and speed converter.
        #       All converters are based on the multiplication of factor and value minus the temperature converter
        #       Temperature converter are based on the original formula.
        #       Each converter has a dictionary collection of factor and a list that defines each converter.
        #       Length converter

        self.meters = {'Miles': 0.0006, 'Yards': 1.092, 'Feet': 3.278, 'Inches': 40, 'Leagues': 0.0002,
                       'Nautical Miles': 0.000539, 'Kilometers': 0.001}
        self.miles = {'Meters': 1609, 'Yards': 1760, 'Feet': 5280, 'Inches': 63360, 'Leagues': 0.333,
                      'Nautical Miles': 0.868, 'Kilometers': 1.60934}
        self.yards = {'Miles': 0.00056, 'Meters': 0.915, 'Feet': 3, 'Inches': 36, 'Leagues': 0.0018,
                      'Nautical Miles': 0.000493, 'Kilometers': 0.0009144}
        self.feet = {'Miles': 0.00018, 'Meters': 0.305, 'Yards': 0.333, 'Inches': 12, 'Leagues': 0.0000631,
                     'Nautical Miles': 0.000164, 'Kilometers': 0.0003048}
        self.inches = {'Miles': 0.0000157, 'Meters': 0.025, 'Feet': 0.083, 'Yards': 12, 'Leagues': 0.0000526,
                       'Nautical Miles': 0.000164, 'Kilometers': 0.0000254}
        self.leagues = {'Miles': 3, 'Meters': 4828, 'Feet': 15840, 'Yards': 5280, 'Inches': 190080,
                        'Nautical Miles': 2.60, 'Kilometers': 4.828}
        self.nautical_miles = {'Miles': 1.15, 'Meters': 1852, 'Feet': 6076.12, 'Yards': 2025.36, 'Inches': 729134,
                               'Leagues': 0.383, 'Kilometers': 1.852}
        self.kilometers = {'Miles': 0.621, 'Meters': 1000, 'Yards': 1093.61, 'Feet': 3280.84, 'Inches': 39370.1,
                           'Nautical Miles': 0.539, 'Leagues': 0.207}
        self.length = [self.meters, self.miles, self.yards, self.feet, self.inches, self.leagues, self.nautical_miles,
                       self.kilometers]
        self.dict_length = {'Meters': 0, 'Miles': 1, 'Yards': 2, 'Feet': 3, 'Inches': 4, 'Leagues': 5,
                            'Nautical Miles': 6, 'Kilometers': 7}
        self.list_length = [self.length, self.dict_length, 'Length converter']

        #       Weight converter
        self.kilograms = {'Pounds': 2.202, 'Ounces': 35.33, 'Short Tons': 0.0011, 'Stones': 0.157, 'Tons': 0.001,
                          'Long Tons': 0.00098}
        self.pounds = {'Kilograms': 0.454, 'Ounces': 16, 'Short Tons': 0.0005, 'Stones': 0.071, 'Tons': 0.00045,
                       'Long Tons': 0.000446}
        self.ounces = {'Pounds': 0.062, 'Kilograms': 0.0283, 'Short Tons': 0.00003125, 'Stones': 0.0044,
                       'Tons': 0.0000283, 'Long Tons': 0.0000279}
        self.short_tons = {'Pounds': 2000, 'Kilograms': 907.185, 'Ounces': 32000, 'Stones': 142.857,
                           'Tons': 0.907, 'Long Tons': 0.892}
        self.stones = {'Pounds': 14, 'Kilograms': 6.35, 'Ounces': 224, 'Short Tons': 0.007, 'Tons': 0.006, 'Long Tons':
            0.00625}
        self.tons = {'Pounds': 2204.62, 'Kilograms': 1000, 'Ounces': 35273.91, 'Long Tons': 0.984,
                     'Stones': 157.473, 'Short Tons': 1.102}
        self.long_tons = {'Pounds': 2240, 'Kilograms': 1016.05, 'Ounces': 35840, 'Short Tons': 1.12,
                          'Stones': 160, 'Tons': 1.016}
        self.weight = [self.kilograms, self.pounds, self.ounces, self.short_tons, self.stones, self.tons,
                       self.long_tons]
        self.dict_weight = {'Kilograms': 0, 'Pounds': 1, 'Ounces': 2, 'Short Tons': 3, 'Stones': 4, 'Tons': 5,
                            'Long Tons': 6}
        self.list_weight = [self.weight, self.dict_weight, 'Weight converter']

        #       Surface converter
        self.square_meters = {'Square Yards': 10.764, 'Square Feet': 1.076, 'Square Inches': 15503.87}
        self.square_yards = {'Square Meters': 0.836, 'Square Feet': 9, 'Square Inches': 1296}
        self.square_feet = {'Square Meters': 0.0929, 'Square Yards': 0.111, 'Square Inches': 144}
        self.square_inches = {'Square Meters': 0.00064, 'Square Yards': 0.00077, 'Square Feet': 0.0069}
        self.surface = [self.square_meters, self.square_yards, self.square_feet, self.square_inches]
        self.dict_surface = {'Square Meters': 0, 'Square Yards': 1, 'Square Feet': 2, 'Square Inches': 3}
        self.list_surface = [self.surface, self.dict_surface, 'Surface converter']

        #       Volume converter
        self.liters = {'Cubic Meters': 0.001, 'Cubic Yards': 0.0013, 'Cubic Feet': 0.0353, 'Gallons': 0.473,
                       'Pints': 2.113}
        self.cubic_meters = {'Liters': 1000, 'Cubic Yards': 1.307, 'Cubic Feet': 35.335, 'Gallons': 264.172,
                             'Pints': 2113.38}
        self.cubic_yards = {'Liters': 756, 'Cubic Meters': 0.756, 'Cubic Feet': 27, 'Gallons': 201.974,
                            'Pints': 1615.79}
        self.cubic_feet = {'Liters': 28.3, 'Cubic Meters': 0.0283, 'Cubic Yards': 0.037, 'Gallons': 7.480,
                           'Pints': 59.844}
        self.gallons = {'Liters': 3.78, 'Cubic Meters': 0.00378, 'Cubic Yards': 0.00495, 'Cubic Feet': 0.164,
                        'Pints': 8}
        self.pints = {'Liters': 0.473, 'Cubic Meters': 0.00047, 'Cubic Yards': 0.000619, 'Cubic Feet': 0.0167,
                      'Gallons': 0.125}
        self.volume = [self.liters, self.cubic_meters, self.cubic_yards, self.cubic_feet, self.gallons, self.pints]
        self.dict_vol = {'Liters': 0, 'Cubic Meters': 1, 'Cubic Yards': 2, 'Cubic Feet': 3, 'Gallons': 4, 'Pints': 5}
        self.list_volume = [self.volume, self.dict_vol, 'Volume converter']

        #       Speed converter
        self.meters_second = {'Yards per second': 1.093, 'Kilometers per hour': 3.6, 'Miles per hour': 2.236}
        self.yards_second = {'Meters per second': 0.914, 'Kilometers per hour': 3.292, 'Miles per hour': 2.045}
        self.kilometers_hour = {'Meters per second': 0.277, 'Yards per second': 0.303, 'Miles per hour': 0.62}
        self.miles_hour = {'Meters per second': 0.477, 'Yards per second': 0.488, 'Kilometers per hour': 1.609}
        self.speed = [self.meters_second, self.yards_second, self.kilometers_hour, self.miles_hour]
        self.dict_speed = {'Meters per second': 0, 'Yards per second': 1, 'Kilometers per hour': 2,
                           'Miles per hour': 3}
        self.list_speed = [self.speed, self.dict_speed, 'Speed converter']

        #       Temperature converter
        self.fahrenheit = {'Celsius': 1.8, 'Kelvin': 1.8}
        self.celsius = {'Fahrenheit': 0.55555, 'Kelvin': 1}
        self.kelvin = {'Celsius': 1, 'Fahrenheit': 0.55555}
        self.temperature = [self.kelvin, self.celsius, self.fahrenheit]
        self.dict_temperature = {'Kelvin': 0, 'Celsius': 1, 'Fahrenheit': 2}
        self.list_temperature = [self.temperature, self.dict_temperature, 'Temperature']

        #       Funny converter: There are funny weight converter, funny beer converter, funny cooking converter and funny surface converter.
        #       The converter follow the same mechanic of Measure converter
        self.humans = {'Elephants': 0.0136, 'Cows': 0.104, 'Rabbits': 27.77, 'Mice': 2500, 'Whales': 0.000535}
        self.elephants = {'Humans': 73.33, 'Cows': 7.638, 'Rabbits': 2037.037, 'Mice': 183333.33, 'Whales': 0.039}
        self.cows = {'Humans': 9.6, 'Elephants': 0.1309, 'Rabbits': 266.66, 'Mice': 24000, 'Whales': 0.00514}
        self.rabbits = {'Humans': 0.036, 'Elephants': 0.000490, 'Cows': 0.00375, 'Mice': 90, 'Whales': 0.0000192}
        self.mice = {'Humans': 0.0004, 'Elephants': 0.00000545, 'Cows': 0.0000416, 'Rabbits': 0.011,
                     'Whales': 0.000000214}
        self.whales = {'Humans': 1866.666, 'Cows': 194.444, 'Elephants': 25.45, 'Rabbits': 51851.85, 'Mice': 4666666.66}
        self.f_weight = [self.humans, self.elephants, self.cows, self.rabbits, self.mice, self.whales]
        self.dict_f_weight = {'Humans': 0, 'Elephants': 1, 'Cows': 2, 'Rabbits': 3, 'Mice': 4, 'Whales': 5}
        self.list_f_weight = [self.f_weight, self.dict_f_weight, 'Animal Converter']

        #       Beer converter
        self.barrels = {'Pints': 88.028, 'Half pints': 176.056, 'Beer cane': 250, 'October fest jars': 50}
        self.f_pints = {'Barrels': 0.011, 'Half pints': 2, 'Beer cane': 2.68, 'October fest jars': 0.568}
        self.half_pints = {'Barrels': 0.0055, 'Pints': 0.5, 'Beer cane': 1.42, 'October fest jars': 0.284}
        self.beer_cane = {'Barrels': 0.004, 'Pints': 0.352, 'Half pints': 0.704, 'October fest jars': 0.2}
        self.october_fest_jar = {'Barrels': 0.004, 'Pints': 1.76, 'Half pints': 3.521, 'Beer cane': 5}
        self.f_volume = [self.barrels, self.f_pints, self.half_pints, self.beer_cane, self.october_fest_jar]
        self.dict_f_volume = {'Barrels': 0, 'Pints': 1, 'Half pints': 2, 'Beer cane': 3, 'October fest jars': 4}
        self.list_f_volume = [self.f_volume, self.dict_f_volume, 'Beer Converter']

        #       Surface converter
        self.soccer = {'Basketball': 19.64, 'Football': 1.542, 'Tennis': 42.172, 'Baseball': 50}
        self.basketball = {'Soccer': 0.05, 'Tennis': 2, 'Football': 0.078, 'Baseball': 0.0525}
        self.football = {'Soccer': 0.6484, 'Basketball': 12.73, 'Tennis': 27.34, 'Baseball': 0.668}
        self.tennis = {'Soccer': 0.023, 'Basketball': 0.815, 'Football': 0.036, 'Baseball': 0.0244}
        self.baseball = {'Soccer': 0.969, 'Basketball': 19.04, 'Tennis': 40.89, 'Football': 1.495}
        self.f_surface = [self.soccer, self.basketball, self.football, self.tennis, self.baseball]
        self.dict_f_surface = {'Soccer': 0, 'Basketball': 1, 'Football': 2, 'Tennis': 3, 'Baseball': 4}
        self.list_f_surface = [self.f_surface, self.dict_f_surface, 'Sports playing fields']

        #       Funny cooking converter
        self.gallons = {'Quarts': 4, 'Pints': 8, 'Cups': 16, 'Ounces': 128, 'Liters': 3.8, 'Milliliters': 3800,
                        'Table Spoons': 253.33, 'Tea Spoons': 760}
        self.quarts = {'Gallons': 0.25, 'Pints': 2, 'Cups': 4, 'Ounces': 32, 'Liters': 0.92, 'Milliliters': 920,
                       'Table Spoons': 61.33, 'Tea Spoons': 184}
        self.pints = {'Gallons': 0.125, 'Quarts': 0.5, 'Cups': 2, 'Ounces': 16, 'Liters': 0.480, 'Milliliters': 480,
                      'Table Spoons': 32, 'Tea Spoons': 96}
        self.cups = {'Gallons': 0.0625, 'Quarts': 0.25, 'Pints': 0.5, 'Ounces': 8, 'Liters': 0.240, 'Milliliters': 240,
                     'Table Spoons': 16, 'Tea Spoons': 48}
        self.ounces = {'Gallons': 0.0078, 'Quarts': 0.031, 'Pints': 0.0625, 'Cups': 0.125, 'Liters': 0.03,
                       'Milliliters': 30, 'Table Spoons': 2, 'Tea Spoons': 6}
        self.liters = {'Gallons': 0.263, 'Quarts': 1.05, 'Pints': 2.1, 'Cups': 4.21, 'Ounces': 33.68,
                       'Milliliters': 1000, 'Table Spoons': 66.66, 'Tea Spoons': 200}
        self.milliliters = {'Gallons': 0.000263, 'Quarts': 0.00105, 'Pints': 0.0021, 'Cups': 0.00421, 'Ounces': 0.03368,
                            'Liters': 0.001, 'Table Spoons': 0.066, 'Tea Spoons': 0.2}
        self.table_spoons = {'Gallons': 0.0039, 'Quarts': 0.0156, 'Pints': 0.031, 'Cups': 0.0625, 'Ounces': 0.5,
                             'Liters': 0.015, 'Milliliters': 15, 'Tea Spoons': 3}
        self.tea_spoons = {'Gallons': 0.0013, 'Quarts': 0.0054, 'Pints': 0.0104, 'Cups': 0.020, 'Ounces': 0.16,
                           'Liters': 0.005, 'Milliliters': 5, 'Table Spoons': 0.33}
        self.f_kitchen = [self.gallons, self.quarts, self.pints, self.cups, self.ounces, self.liters, self.milliliters,
                          self.table_spoons, self.tea_spoons]
        self.dict_f_kitchen = {'Gallons': 0, 'Quarts': 1, 'Pints': 2, 'Cups': 3, 'Ounces': 4, 'Liters': 5,
                               'Milliliters': 6, 'Table Spoons': 7, 'Tea Spoons': 8}
        self.list_f_kitchen = [self.f_kitchen, self.dict_f_kitchen, 'Funny cooking']

        #       Currency converter: This converter follow a different way. We create a ticker for yfinance with the
        #       dictionary’s values. Then we multiplicate exchange factor and the value.
        self.currencies = {'US Dollar': 'USD', 'Euro': 'EUR', 'Pound': 'GBP', 'Canadian Dollar': 'CAD',
                           'Australian Dollar': 'AUD', 'New Zealand Dollar': 'NZD',
                           'Swiss Franc': 'CHF', 'Singapore Dollar': 'SGD', 'Hong Kong Dollar': 'HKD',
                           'Swedish Crown': 'SEK', 'Norwegian Crown': 'NOK', 'Danish Crown': 'DKK',
                           'Chinese Yuan': 'CNY'}
        self.list_currency = [key for key in self.currencies]

        #       Create the main menu window in the builder class
        self.root = Tk()
        self.root.title('Unit Converter - Main Menu')
        self.root.geometry(self.screen_size)
        self.root.resizable(10, 10)

        #       Stylizing the interface
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family=self.font, size=14, weight=font.BOLD)
        self.style = ttk.Style(self.root)
        self.style.configure('TButton', background=self.background_color1, relief='raised')
        self.style.configure('TLabel', background=self.background_color2)
        self.style.configure('TEntry', background=self.background_color1)
        self.style.configure('TCombobox', background=self.background_color1, fieldbackground=self.background_color1,
                             darkcolor=self.background_color2, arrowcolor=self.element_color)
        self.style.configure('TFrame', background=self.background_color2)
        self.root.configure(bg=self.background_color2)

        #       Create and pack the frames for menu structure
        self.frame_title = ttk.Frame(self.root)
        self.frame_menu = ttk.Frame(self.root)
        self.frame_nav = ttk.Frame(self.root)
        self.frame_title.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.frame_menu.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.frame_nav.pack(side=TOP, expand=True, padx=10, pady=5)

        #       Graphical Interface Variables(Values)
        self.var_unit1 = StringVar()
        self.var_unit2 = StringVar()
        self.first_coin = StringVar()
        self.second_coin = StringVar()
        self.answer = StringVar()
        self.value = DoubleVar(value=0.0)

        #       Main menu functions
        #       exit1 function
        def exit1():
            self.root.destroy()
        #       Labels and buttons from main menu
        self.Main_Label = ttk.Label(self.frame_title, text='Unit Converter', anchor='center')
        self.Secondary_Label = ttk.Label(self.frame_title, text='Main Menu', anchor='center')
        self.Separator = ttk.Separator(self.frame_title, orient='horizontal')
        self.Button_Converter = ttk.Button(self.frame_menu, text='Measure Converter', command=self.converter)
        self.Button_Funny = ttk.Button(self.frame_menu, text='Funny Converter', command=self.funny)
        self.Button_Currency = ttk.Button(self.frame_menu, text='Currency Converter', command=self.currency)
        self.Separator2 = ttk.Separator(self.frame_menu, orient='horizontal')
        self.Button_Exit1 = ttk.Button(self.frame_nav, text='Exit', command=exit1)

        #       Format labels
        self.Main_Label.config(font=(self.font, 20, font.BOLD))
        self.Secondary_Label.config(font=(self.font, 15, font.BOLD))

        #       Labels and windows pack
        self.Main_Label.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Secondary_Label.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Separator.pack(fill='x')
        self.Button_Converter.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.Button_Funny.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.Button_Currency.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.Separator2.pack(fill='x')
        self.Button_Exit1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.root.mainloop()

    #   Method converter (Submenu - Measure converter)
    def converter(self):
        #       Unit converter functions
        #           exit2 function
        def exit2():
            self.root2.destroy()
            self.root.destroy()
        #           back function
        def back():
            self.root2.destroy()
        #       Create the measure convert submenu window
        self.root2 = Toplevel()
        self.root2.geometry(self.screen_size)
        self.root2.resizable(10, 10)
        self.root2.title('Unit Converter - Measure Converter Menu')
        self.root2.configure(bg=self.background_color2)
        #       Create and pack the frames for Measure menu structure
        self.frame_title2 = ttk.Frame(self.root2, width=600, height=150)
        self.frame_menu2 = ttk.Frame(self.root2, width=600, height=400)
        self.frame_nav2 = ttk.Frame(self.root2, width=600, height=50)
        self.frame_title2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.frame_menu2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.frame_nav2.pack(side=TOP, fill=X, expand=True, padx=10, pady=10)
        #       Labels and Buttons for measure convert submenu
        self.Main_Label2 = ttk.Label(self.frame_title2, text='Unit Converter', anchor='center')
        self.Secondary_Label2 = ttk.Label(self.frame_title2, text='Measure Converter', anchor='center')
        self.Separator3 = ttk.Separator(self.frame_title2, orient='horizontal')
        self.Button_Weight = ttk.Button(self.frame_menu2, text='WEIGHT',
                                        command=lambda: self.unit_converter(self.list_weight, self.root2))
        self.Button_Speed = ttk.Button(self.frame_menu2, text='SPEED',
                                       command=lambda: self.unit_converter(self.list_speed, self.root2))
        self.Button_Temperature = ttk.Button(self.frame_menu2, text='TEMPERATURE',
                                             command=lambda: self.unit_converter(self.list_temperature, self.root2))
        self.Button_Surface = ttk.Button(self.frame_menu2, text='SURFACE',
                                         command=lambda: self.unit_converter(self.list_surface, self.root2))
        self.Button_Length = ttk.Button(self.frame_menu2, text='LENGTH',
                                        command=lambda: self.unit_converter(self.list_length, self.root2))
        self.Button_Volume = ttk.Button(self.frame_menu2, text='VOLUME',
                                        command=lambda: self.unit_converter(self.list_volume, self.root2))
        self.Separator4 = ttk.Separator(self.frame_menu2, orient='horizontal')
        self.Button_Back = ttk.Button(self.frame_nav2, text='BACK', command=back)
        self.Button_Exit2 = ttk.Button(self.frame_nav2, text='EXIT', command=exit2)

        #       Format labels
        self.Main_Label2.config(font=(self.font, 20, font.BOLD), justify='center')
        self.Secondary_Label2.config(font=(self.font, 15, font.BOLD), justify='center')

        #       Labels and windows pack
        self.Main_Label2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Secondary_Label2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Separator3.pack(fill='x')
        self.Button_Weight.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.Button_Speed.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.Button_Temperature.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.Button_Surface.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.Button_Length.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.Button_Volume.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.Separator4.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Button_Back.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        self.Button_Exit2.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

        #       Root2 config
        self.root2.transient(master=self.root)
        self.root2.grab_set()
        self.root2.wait_window(self.root2)

    #       Method converter (Submenu - funny converter)
    def funny(self):
        #       Create the funny convert submenu window
        self.root3 = Toplevel()
        self.root3.geometry(self.screen_size)
        self.root3.resizable(10, 10)
        self.root3.title('Unit Converter - Funny Converter Menu')
        self.root3.configure(bg=self.background_color2)

        #       Create and pack the frames for menu structure
        self.frame_title3 = ttk.Frame(self.root3, width=600, height=150)
        self.frame_menu3 = ttk.Frame(self.root3, width=600, height=400)
        self.frame_nav3 = ttk.Frame(self.root3, width=600, height=50)
        self.frame_title3.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.frame_menu3.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.frame_nav3.pack(side=TOP, fill=X, expand=True, padx=10, pady=10)

        #       Funny converter functions
        #       exit3 function
        def exit3():
            self.root3.destroy()
            self.root.destroy()

        #       back function
        def back3():
            self.root3.destroy()

        #       Labels and Buttons for funny convert submenu
        self.Main_Label3 = ttk.Label(self.frame_title3, text='Unit Converter', anchor='center')
        self.Secondary_Label3 = ttk.Label(self.frame_title3, text='Funny Converter', anchor='center')
        self.Separator5 = ttk.Separator(self.frame_title3, orient='horizontal')
        self.Button_f_Volume = ttk.Button(self.frame_menu3, text='BEER CONTAINERS',
                                          command=lambda: self.unit_converter(self.list_f_volume, self.root3))
        self.Button_f_Weight = ttk.Button(self.frame_menu3, text='ANIMAL CONVERTER',
                                          command=lambda: self.unit_converter(self.list_f_weight, self.root3))
        self.Button_f_Surface = ttk.Button(self.frame_menu3, text='SPORTS PLAYING FIELD',
                                           command=lambda: self.unit_converter(self.list_f_surface, self.root3))
        self.Button_f_Cooking = ttk.Button(self.frame_menu3, text='FUNNY COOKING',
                                           command=lambda: self.unit_converter(self.list_f_kitchen, self.root3))
        self.Separator6 = ttk.Separator(self.frame_menu3, orient='horizontal')
        self.Button_Back3 = ttk.Button(self.frame_nav3, text='BACK', command=back3)
        self.Button_Exit3 = ttk.Button(self.frame_nav3, text='EXIT', command=exit3)

        #       Format labels
        self.Main_Label3.config(font=(self.font, 20, font.BOLD), justify='center')
        self.Secondary_Label3.config(font=(self.font, 15, font.BOLD), justify='center')

        #       Labels and windows pack
        self.Main_Label3.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Secondary_Label3.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Separator5.pack(fill='x')
        self.Button_f_Volume.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.Button_f_Weight.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.Button_f_Surface.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.Button_f_Cooking.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.Separator6.pack(fill='x')
        self.Button_Back3.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        self.Button_Exit3.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

        #       Root3 config
        self.root3.transient(master=self.root)
        self.root3.grab_set()
        self.root.wait_window(self.root3)

    #   Method for unit_converter
    def unit_converter(self, list, root):
        self.root4 = Toplevel()
        self.root4.geometry(self.screen_size)
        self.root4.resizable(10, 10)
        self.root4.title('Unit Converter - ' + list[2])
        self.root4.configure(bg=self.background_color2)

        #       Create and pack the frames for menu structure
        self.frame_title4 = ttk.Frame(self.root4, width=600, height=150)
        self.frame_menu4 = ttk.Frame(self.root4, width=600, height=400)
        self.frame_nav4 = ttk.Frame(self.root4, width=600, height=50)
        self.frame_title4.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.frame_menu4.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.frame_nav4.pack(side=TOP, fill=X, expand=True, padx=10, pady=10)

        #       Specific Variables:
        self.list_units = [key for key in list[1]]

        #       Basic unit converter functions
        #       back function

        def back():
            self.root4.destroy()

        #       Labels and Buttons for measure convert submenu
        self.Main_Label = ttk.Label(self.frame_title4, text='Unit Converter', anchor='center')
        self.Secondary_Label = ttk.Label(self.frame_title4, text=list[2], anchor='center')
        self.Separator7 = ttk.Separator(self.frame_title4, orient='horizontal')
        self.Menu_Unit1 = ttk.Combobox(self.frame_menu4, state='readonly', values=self.list_units,
                                       textvariable=self.var_unit1)
        self.Menu_Unit1.set('Select the first unit')
        self.Entry_Label = ttk.Label(self.frame_menu4, text='Enter the value')
        self.Entry_Value = ttk.Entry(self.frame_menu4, textvariable=self.value)
        self.Menu_Unit2 = ttk.Combobox(self.frame_menu4, state='readonly', values=self.list_units,
                                       textvariable=self.var_unit2)
        self.Menu_Unit2.set('Select the second unit')
        self.Button_Convert = ttk.Button(self.frame_menu4, text='CONVERT!', command=lambda: self.convert(list))
        self.Result = ttk.Entry(self.frame_menu4, textvariable=self.answer, justify='center')
        self.Separator8 = ttk.Separator(self.frame_menu4, orient='horizontal')
        self.Button_Back4 = ttk.Button(self.frame_nav4, text='BACK', command=back)

        #       Format widgets
        self.Main_Label.config(font=(self.font, 20, font.BOLD), justify='center')
        self.Secondary_Label.config(font=(self.font, 15, font.BOLD), justify='center')
        self.Entry_Value.config(font=(self.font, 14, font.BOLD))
        self.Result.config(font=(self.font, 14, font.BOLD))
        self.Menu_Unit1.config(font=(self.font, 10, font.BOLD))
        self.Menu_Unit2.config(font=(self.font, 10, font.BOLD))

        #       Labels and windows pack
        self.Main_Label.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Secondary_Label.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Separator7.pack(fill='x')
        self.Menu_Unit1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Menu_Unit2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Entry_Label.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Entry_Value.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Button_Convert.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Separator8.pack(fill='x')
        self.Button_Back4.pack(side=BOTTOM, expand=True, padx=10, pady=10)
        self.root4.transient(master=root)
        self.root4.grab_set()
        self.root.wait_window(self.root4)

    #   Method for plot the unit converter graphics
    def plot(self, unit, unit2, dict):
        try:
            self.root4.geometry('1200x600')
            self.Result.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
            all_units = [dict[key] for key in dict]
            all_units_keys = [key for key in dict]
            y = [1 / i for i in all_units]
            x = [(i / len(dict)) for i in range(len(dict))]
            fig, a = plt.subplots(1, 2, figsize=(60, 20), facecolor='#CAB48F')
            a[0].barh(x, y, height=0.02, color=self.plot_color)
            a[0].set_facecolor(self.facecolor_plot2)
            a[0].set_yticks(x, all_units_keys,
                            fontweight='bold',
                            fontfamily='Sans',
                            fontname=self.font)
            a[0].set_xticks([1], [unit],
                            fontweight='bold',
                            fontfamily='Sans',
                            fontname=self.font)
            a[0].set_title('Relationship between {} and other units'.format(unit),
                           fontweight='bold',
                           fontsize=11,
                           fontfamily='Sans',
                           fontname=self.font)
            a[0].plot([1, 1], [0, 1], c='black')
            a[0].set_xlim([0, 3])
            x2 = [0.3, 0.6]
            y2 = [1, 1 / dict[unit2]]
            a[1].bar(x2, y2, width=0.2, color=self.plot_color2)
            a[1].set_facecolor(self.facecolor_plot2)
            a[1].set_yticks([])
            a[1].set_xticks(x2, [unit, unit2],
                            fontweight='bold',
                            fontfamily='Sans',
                            fontname=self.font)
            a[1].set_title('Relationship between {} and {}'.format(unit, unit2),
                           fontweight='bold',
                           fontsize=11,
                           fontfamily='Sans',
                           fontname=self.font)
            self.canvas = FigureCanvasTkAgg(fig, master=self.frame_nav4)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
            self.Button_Back.pack(side=BOTTOM, expand=True, padx=10, pady=10)
        except ValueError:
            messagebox.showerror("ERROR!", "The value must be a number", parent=self.root4)

    #   convert method gives us the result of multiplying the value by the factor
    def convert(self, list):
        data_error = False
        try:
            global unit1
            global unit2
            global value
            unit1 = self.var_unit1.get()
            unit2 = self.var_unit2.get()
            value = self.value.get()
        except:
            data_error = True
        if not data_error:
            self.Menu_Unit1.destroy()
            self.Menu_Unit2.destroy()
            self.Entry_Label.destroy()
            self.Entry_Value.destroy()
            self.Button_Convert.destroy()
            if unit1 == 'Select the first unit' and unit2 == 'Select the second unit':
                self.answer.set('0')
            elif unit1 == unit2:
                answer1 = str(value) + " " + unit1
                self.answer.set(answer1)

            #           In the case of temperature there is an exception because it depends on a formula
            elif list == self.list_temperature:
                if unit1 == 'Celsius':
                    if unit2 == 'Fahrenheit':
                        answer2 = 9 * value / 5 + 32
                        answer2 = round(answer2, 2)
                    else:
                        answer2 = value + 273.15
                        answer2 = round(answer2, 2)
                    self.plot(unit1, unit2, list[0][list[1][unit1]])
                elif unit1 == 'Kelvin':
                    if unit2 == 'Celsius':
                        answer2 = value - 273.15
                        answer2 = round(answer2, 2)
                    else:
                        answer2 = 9 * (value - 273.15) / 5 + 32
                        answer2 = round(answer2, 2)
                    self.plot(unit1, unit2, list[0][list[1][unit1]])
                else:
                    if unit2 == 'Celsius':
                        answer2 = 5 * (value - 32) / 9
                        answer2 = round(answer2, 2)
                    else:
                        answer2 = 5 * (value - 32) / 9 + 273.15
                        answer2 = round(answer2, 2)
                    self.plot(unit1, unit2, list[0][list[1][unit1]])
                answer3 = str(value) + " " + unit1 + " are " + str(answer2) + " " + unit2
                self.answer.set(answer3)
            else:
                factor = list[0][list[1][unit1]][unit2]
                answer2 = str(value) + " " + unit1 + " are " + str(value * factor) + " " + unit2
                self.answer.set(answer2)
                self.plot(unit1, unit2, list[0][list[1][unit1]])

        #       Since all the data is preset in the combobox except the value,
        #       we can only have a data error when entering characters other than numbers
        else:
            messagebox.showerror("ERROR!", "The value must be a number", parent=self.root4)

    #   method for currency menu
    def currency(self):
        self.root5 = Toplevel()
        self.root5.geometry(self.screen_size)
        self.root5.resizable(10, 10)
        self.root5.title('Unit Converter - ' + 'Currency Converter')
        self.root5.configure(bg=self.background_color2)

        #       Create and pack the frames for menu structure
        self.frame_title5 = ttk.Frame(self.root5, width=600, height=150)
        self.frame_menu5 = ttk.Frame(self.root5, width=600, height=400)
        self.frame_nav5 = ttk.Frame(self.root5, width=600, height=50)
        self.frame_title5.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.frame_menu5.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
        self.frame_nav5.pack(side=TOP, fill=X, expand=True, padx=10, pady=10)

        #       Currency converter functions
        #       back function
        def back():
            self.root5.destroy()

        #       Labels and Buttons for currency convert submenu
        self.Main_Label5 = ttk.Label(self.frame_title5, text='Unit Converter', anchor='center')
        self.Secondary_Label5 = ttk.Label(self.frame_title5, text='Currency Converter', anchor='center')
        self.Separator9 = ttk.Separator(self.frame_title5, orient='horizontal')
        self.Menu_Coins1 = ttk.Combobox(self.frame_menu5, state='readonly', values=self.list_currency,
                                        textvariable=self.first_coin)
        self.Menu_Coins1.set('Select the first unit')
        self.Entry_Label5 = ttk.Label(self.frame_menu5, text='Enter the value')
        self.Entry_Value5 = ttk.Entry(self.frame_menu5, textvariable=self.value)
        self.Menu_Coins2 = ttk.Combobox(self.frame_menu5, state='readonly', values=self.list_currency,
                                        textvariable=self.second_coin)
        self.Menu_Coins2.set('Select the second unit')
        self.Button_Change = ttk.Button(self.frame_menu5, text='CHANGE!', command=lambda: self.change())
        self.Result3 = ttk.Entry(self.frame_menu5, textvariable=self.answer, justify='center')
        self.Separator10 = ttk.Separator(self.frame_menu5, orient='horizontal')
        self.Button_Back5 = ttk.Button(self.frame_nav5, text='BACK', command=back)

        #       Format widgets
        self.Main_Label5.config(font=(self.font, 20, font.BOLD), justify='center')
        self.Secondary_Label5.config(font=(self.font, 15, font.BOLD), justify='center')
        self.Entry_Value5.config(font=(self.font, 14, font.BOLD))
        self.Result3.config(font=(self.font, 14, font.BOLD))
        self.Menu_Coins1.config(font=(self.font, 10, font.BOLD))
        self.Menu_Coins2.config(font=(self.font, 10, font.BOLD))

        #       Labels and windows pack
        self.Main_Label5.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Secondary_Label5.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Separator9.pack(fill='x')
        self.Menu_Coins1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Menu_Coins2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Entry_Label5.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Entry_Value5.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Button_Change.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.Separator10.pack(fill='x')
        self.Button_Back5.pack(side=BOTTOM, expand=True, padx=10, pady=10)
        self.root5.transient(master=self.root)
        self.root5.grab_set()
        self.root.wait_window(self.root5)

    #   Method for plot the change
    def plot_change(self):
        try:
            import yfinance as yf
            import pandas as pd
            try:
                first_coint = self.currencies[self.first_coin.get()]
                currencies_1 = self.currencies
                del (currencies_1[self.first_coin.get()])
                currency_name = currencies_1.keys()
                currency_tickers = [(first_coint + currencies_1[i] + '=X') for i in currency_name]
                currency_values = [(yf.download(ticker, period='1d', interval='1m')['Close'].iloc[-1]) for ticker in
                                   currency_tickers]
                self.root5.geometry(self.screen_size2)
                fig = plt.figure(facecolor=self.facecolor_plot)
                plt.bar([i for i in range(len(currency_name))], currency_values, color=self.plot_color)
                plt.plot([-1, 12], [1, 1], color='black')
                plt.grid()
                title = 'Currency exchange rate for {}'.format(self.first_coin.get())
                plt.title(title,
                          fontweight='bold',
                          fontfamily='Sans',
                          fontname=self.font
                          )
                plt.xticks([i for i in range(len(currency_name))],
                           [self.currencies[name] for name in currency_name],
                           fontweight='bold',
                           fontfamily='Sans',
                           fontname=self.font
                           )
                labels = [i for i in range(int(max(currency_values)) + 2)]
                labels[1] = first_coint
                plt.yticks([i for i in range(int(max(currency_values)) + 2)],
                           labels,
                           fontweight='bold',
                           fontfamily='Sans',
                           fontname=self.font
                           )
                plt.tight_layout()
                self.canvas = FigureCanvasTkAgg(fig, master=self.frame_nav5)
                self.canvas.draw()
                self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)
                self.currencies[self.first_coin.get()] = first_coint
            except ValueError:
                messagebox.showerror("ERROR!", "The value must be a number", parent=self.root5)

        except FileNotFoundError:
            messagebox.showerror("ERROR!", "Libraries yfinance and pandas are mandatory for currency"
                                           " converter", parent=self.root5)

    #   Method for currency change
    def change(self):
        try:
            import yfinance as yf
            data_error = False
            try:
                global value
                global first_coint
                global second_coint
                value = float(self.value.get())
                first_coint = self.currencies[str(self.first_coin.get())]
                second_coint = self.currencies[str(self.second_coin.get())]
            except:
                data_error = True
            if not data_error:
                try:
                    ticker = first_coint + second_coint + '=X'
                    exchange = yf.download(ticker, period='1d', interval='1m')['Close'].iloc[-1]
                    total = str(round(exchange * self.value.get(), 2))
                    self.Menu_Coins1.destroy()
                    self.Menu_Coins2.destroy()
                    self.Entry_Label5.destroy()
                    self.Entry_Value5.destroy()
                    self.Button_Change.destroy()
                    self.Result3.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
                    result = '{} {} are {} {}'.format(str(self.value.get()), str(self.first_coin.get()), total,
                                                      str(self.second_coin.get()))
                    self.answer.set(result)
                    self.plot_change()
                except KeyError:
                    messagebox.showerror("ERROR!", "Please introduce two coins", parent=self.root5)
            else:
                messagebox.showerror("ERROR!", "The value must be a number", parent=self.root5)
        except FileNotFoundError:
            messagebox.showerror('ERROR!', 'You must have installed the yf library', parent=self.root5)
            self.root5.destroy()


def main():
    UnitConverter()


if __name__ == '__main__':
    main()