# Word-Doc-2-HTML
Python Desktop application to convert Word Documents to HTML - based on mammoth-python

## Quickstart
Install the application directly from the .exe file you can find [here](application/Word-Doc-2-HTML.0.0.0.exe), then get to use it by clicking on the icon. 

The application will make you choose a .docx file by clicking `Upload Document`. After having uploaded the document, just click `Process document` and you will get an html file output with the same name of your original Word document.

## Developers' section
### Wish to custom?
If you are a developer and you wish to contribute or modify the application, [here](scripts/) you can find the scripts. 

If you wish to get the whole repository, just make sure to clone it by:
```bash
# IF YOU HAVEN'T INITIALIZED YET git IN CURRENT DIR
git init
# CLONE
git clone https://github.com/AstraBert/Word-Doc-2-HTML
```
### How was the app developed?
The application is represented by a simple python framework based on [`mammoth`](https://github.com/mwilliamson/python-mammoth).

The script was turned into an executable Desktop application (OS-independent, it should work on all operative systems) thanks to [`auto-py-to-exe`](https://github.com/brentvollebregt/auto-py-to-exe). 

### Changelog
- **Latest release**:
  0.0.0: base application with all the features descripted above (03/06/2024)
- **Other releases**:
  None

### References
- [`mammoth`](https://github.com/mwilliamson/python-mammoth)
- [`auto-py-to-exe`](https://github.com/brentvollebregt/auto-py-to-exe)

### Author and license
Please consider to cite the author of the app, [Astra Bertelli](https://github.com/AstraBert), if you are using it for your projects. 

The app is provided under [BSD 2-Clause "Simplified" License](LICENSE).

