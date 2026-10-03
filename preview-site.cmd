@echo off
setlocal
set "PATH=%~dp0.tools\node-v24.14.0-win-x64;%PATH%"
call "%~dp0.tools\node-v24.14.0-win-x64\corepack.cmd" pnpm install --frozen-lockfile
call "%~dp0.tools\node-v24.14.0-win-x64\corepack.cmd" pnpm preview
