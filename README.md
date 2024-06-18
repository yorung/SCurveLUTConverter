# SCurveLUTConverter
Convert Technicolor CineStyle S-Curve LUT into cube file.

Technicolor社のCineStyle S-Curve LUTをcube形式に変換します。

## Differences

### S-Curve applied

[![S-Curve applied](https://img.youtube.com/vi/8nE8yoqubQE/0.jpg)](https://www.youtube.com/watch?v=8nE8yoqubQE)

### S-Curve not applied

[![S-Curve not applied](https://img.youtube.com/vi/M_384Pmkkos/0.jpg)](https://www.youtube.com/watch?v=M_384Pmkkos)



## How to run
Just run curve2cube.py in a folder which contains S-curve_for_CineStyle.txt and curve2cube.py together generates S-curve_for_CineStyle.cube. 

S-curve_for_CineStyle.txtとcurve2cube.pyを同じフォルダに置き、curve2cube.pyを実行してください。するとS-curve_for_CineStyle.cubeという名前のファイルが生成されます。

## How to install S-curve_for_CineStyle.cube
In case of DaVinci Resolve on Windows, make a folder with any name just under C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT and place S-curve_for_CineStyle.cube.

WindowsのDaVinci Resolveであれば C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT 以下に任意の名前でフォルダを作り、S-curve_for_CineStyle.cubeを格納することで使えるようになります。

## Background
Technicolor provides Canon DSLR picture style named "CineStyle". But the S-curve provided with the CineStyle doesn't applicable on DaVinci Resolve due to it's format is not supported.

Technicolor社が以下でキヤノン一眼レフカメラ用のピクチャースタイル「CineStyle」を提供しています。同梱のS-curve LUTをDaVinci Resolveで使えなかったため作りました。

https://www.technicolor.com/cinestyle (not available now)
https://web.archive.org/web/20201101115712/https://www.technicolor.com/cinestyle (archive.org)
