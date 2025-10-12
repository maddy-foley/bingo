# Script to generate bingo textboxes in Scribus.

## About

This is a project built for an upcomming special event in my family. We needed many tailored bingo cards and a bingo drawing program.

# Requirements


## Software
* [![Python][Python]][Python-url]

* [![Scribus-logo][Scribus-logo]![Scribus][Scribus]][Scribus-url]
    *  [![Scribus-API][Scribus-API]][Scribus-url]

## Art  & Scribus Document Design Requirements
- Document Size: Portriat U.S Letter Size (8.5" x 11")
- Vector Bingo Table Art (<i>Default Table dimension sizes and position TBD</i>)
    - I used ![inkscape-logo]![inkscape][inkscape] to draw vectors


# Usage

## Data: 

- Traditional bingo takes <strong>*15 string values*</strong> 
JSON File Format:



```
{
    "b": [<15 string values> ... ],
    "i": [...],
    "n": [...],
    "g": [...],
    "o": [...]
}
```
</br>

## RoadMap
1. Design Cards
2. Generate Random Bingo Cards
3. Add a Bingo Random Drawing Program 



[Python]: https://img.shields.io/badge/python3-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors

[Scribus-logo]: assets/Scribus_logo-sm.png
[Scribus]: https://img.shields.io/badge/Scribus-version_1.6+-blue
[Scribus-url]: https://sourceforge.net/projects/scribus/

[Scribus-Api]: https://img.shields.io/badge/Scribus_API-(Built_into_Scribus)-8A2BE2

[Scribus-API-url]:https://wiki.scribus.net/canvas/Scripter_API

[inkscape-logo]: assets/Inkscape_Logo-sm.png
[inkscape]: https://img.shields.io/badge/Inkscape-white
[inkscape-url]: https://inkscape.org/