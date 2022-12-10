{
  "window.zoomLevel": 0.1,
  "editor.formatOnSave": true,
  "code-runner.executorMap": {
    "python": "clear ; .\\venv\\Scripts\\python.exe"
  },
  "code-runner.runInTerminal": true,
  "code-runner.clearPreviousOutput": true,
  // Python
  "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.formatOnSave": true,
    "editor.formatOnType": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  },
  "python.languageServer": "Pylance",
  "python.formatting.autopep8Args": [
    "--indent-size=4"
    // "--ignore=E111",
  ],
  "python.linting.flake8Args": [
    // "--ignore=E111",
  ],
  "python.linting.pylintArgs": [
    "--load-plugins=pylint_django",
    "--errors-only"
  ],
  "python.linting.flake8Enabled": true,
  "python.testing.unittestEnabled": false,
  "python.linting.mypyEnabled": true,
  "python.defaultInterpreterPath": "python",
  "workbench.colorTheme": "OM Theme (Default Dracula Italic)"
}