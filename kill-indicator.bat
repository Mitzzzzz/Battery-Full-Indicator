ECHO ON
TITLE Battery Indicator Kill
REM A batch script to kill the script
taskkill /f /t /fi "windowtitle eq Battery Indicator"
