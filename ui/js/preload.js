const { contextBridge } = require('electron');

// Logowanie, aby upewnić się, że skrypt preload działa
console.log('Preload script is running...');

window.addEventListener('DOMContentLoaded', () => {
  console.log('DOMContentLoaded in preload');

  const script = document.createElement('script');
  script.src = './eel.js';  // Upewnij się, że ścieżka jest poprawna
  script.onload = () => {
    console.log('eel.js loaded');

    contextBridge.exposeInMainWorld('eel', {
      update_status: () => {
        return new Promise((resolve, reject) => {
          eel.update_status()(resolve).catch(reject);
        });
      },
      refresh_contractors: () => {
        return new Promise((resolve, reject) => {
          eel.refresh_contractors()(resolve).catch(reject);
        });
      },
      send_echo: (param) => {
        return new Promise((resolve, reject) => {
          eel.send_echo(param)(resolve).catch(reject);
        });
      }
    });
  };
  script.onerror = () => {
    console.error('Failed to load eel.js');
  };
  document.head.appendChild(script);
});

console.log('Preload script has finished running.');
