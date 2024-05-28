const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');

let mainWindow;

function createWindow() {
  const iconPath = 'C:/Users/JustFazii/Desktop/JF-Enova_Electron/ui/img/enova-logo.ico';
  console.log('Icon path:', iconPath);

  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    minWidth: 600,
    minHeight: 400,
    frame: false,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: true,
      contextIsolation: true,
      devTools: true
    },
    icon: iconPath
  });

  mainWindow.loadURL("http://localhost:8000/index.html");
  mainWindow.setBackgroundColor('#030303')
  mainWindow.webContents.openDevTools();

  mainWindow.on('closed', function () {
    mainWindow = null;
  });

  mainWindow.on('maximize', () => {
    mainWindow.webContents.send('isMaximized');
  });

  mainWindow.on('unmaximize', () => {
    mainWindow.webContents.send('isRestored');
  });
}

app.on("ready", createWindow);

app.on("window-all-closed", function () {
  if (process.platform !== "darwin") app.quit();
});

app.on("activate", function () {
  if (mainWindow === null) createWindow();
});

ipcMain.on('minimizeApp', () => {
  mainWindow.minimize();
});

ipcMain.on('maximizeApp', () => {
  if (mainWindow.isMaximized()) {
    mainWindow.restore();
  } else {
    mainWindow.maximize();
  }
});

ipcMain.on('closeApp', () => {
  mainWindow.close();
});
