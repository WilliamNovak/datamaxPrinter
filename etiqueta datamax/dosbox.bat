cd\
copy C:\SFT\MOVTO\ETIQUETA\LOGO_EMP.JPG C:\SFT\movto\etiqueta\LOGO_EMP.bmp
"C:\Program Files (x86)\IrfanView\i_view32.exe" C:\SFT\MOVTO\ETIQUETA\LOGO_EMP.JPG /bpp=1 /resize=(140,93) /rotate_r /aspectratio /silent /convert=C:\SFT\movto\etiqueta\LOGO_EMP.bmp
C:\SFT\movto\etiqueta\sleep.exe 1
cd\
c:
cd DOSBOX
"DOSBox.exe" -c "mount x C:\SFT\MOVTO\ETIQUETA" -c "x:"  -c etiqueta.bat
