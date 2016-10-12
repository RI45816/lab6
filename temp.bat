for %%F in ("..") do set "folder=%%~nxF"
curl -u "RI45816:Sirius-1029" https://api.github.com/user/repos -d "{\"name\":\"%folder%\"}"
echo "# %folder%" > README.md
git init
git add .
git commit -a -m "first commit"
git remote add origin https://github.com/RI45816/HW5.git
git remote set-url origin https://github.com/RI45816/HW5.git
git push -u origin master

