# Installation & In-code changes

**Do the following before running the code.**

- Open CMD/Terminal and navigate to the folder.

- Type `pip install virtualenv` and let it install

- Create a virtual environment and activate it. 

  ```
  python -m venv env
  ```

  Then, depending on your operating system; use the following code to activate the virtual environment. You will see (env) in your console.

  *Windows* - `env\Scripts\activate.bat`

  *Linux/macOS* - `source env/bin/activate`

- Now, let's install the packages using pip. Paste the following and let it install. Make sure to install any packages within the virtual env.

  `pip install -r requirements.txt`

- Depending on your OS, follow the below steps to solve the SpeechRecognition module error. 

  - *Windows* (open CMD as an Administrator)

    `pip install winspeech`

    `pip install PyAudio`

    `pip install SpeechRecognition`

  - *macOS/Linux*

    1. Install Xcode - Command Line tools. Type `Xcode-select —install` in the terminal (macOS only)

    2. Install [Brew](http://brew.sh/)

    3. `sudo brew install portaudio`

    4. `sudo pip install pyaudio`

    5. `pip install SpeechRecognition`

       

  You can now run the python file to start Genie! Simply type `python3 main.py` into the console.

# In-code changes

**You need to do some small changes in the code to personalize Genie for you. **

### Changing app locations

In the `os_func.py` file, you'll need to change the location of the apps according to your system. Locate the .exe file of that app your want and copy its path (Windows). 

In macOS, open the Applications folder. While holding down the “Control” button, click on the app you want to copy the path of in Finder. Press the “Option” key (In the menu that appears after step one, you'll see “Copy” turn into “Copy [file path name] as Pathname”. ) Select “Copy [file path name] as Pathname”. Refer to [this website](https://setapp.com/how-to/how-to-find-the-path-of-a-file-in-mac#:~:text=While%20holding%20down%20the%20%E2%80%9CControl,file%20path%20name%5D%20as%20Pathname%E2%80%9D) for easier understanding.

### Initialising the Engine

In line 22 in the `main.py` file, you can see that 'nsss' is set because I used a Mac system to develop this assistant. Now depending on your operating system, use 'sapi5' for Windows, 'nsss' for macOS and 'eSpeak' for Linux. 

### Changing the screenshot folder location

On line 141 in the `main.py` file, replace `r'/Users/setukumar/Desktop/Screenshots/Screenshot.png'` in the brackets with r'your_folder_path'.