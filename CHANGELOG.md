# CHANGELOG

> This file serves as the journel for this project.

> 4/4/19, Harry Dunham:
> Abstract Implementation of the Input Screen. This 
includes basic text inputs and a non-functioning submit
button (inputs include: tracking number, current date, 
bin number, etc.) . This is meant to get a visual 
understanding of what the input screen should look like.

>4/6/19, Harry Dunham:
Implemented the entire UI for the screen. This entailed the creation of
a grid layout that encompasses the entire screen. This screen is divided into
three BoxLayouts. The first is a simple Status button that displays whether
package submission was successful. Next, is the input fields for the package, as
mentioned before this has: tracking number textinput, staff-id, etc.
Additionally, a selection system was added at the bottom  of the input fields
for the carrier id. It is simply 5 buttons arrayed in a line that allows the
user to select the package's carrier.

> 4/8/19, Harry Dunham:
Fixed the carrier implementation so that whenever one carrier is
selected all the other carriers are deselected. Also if the user selects the
currently selected carrier it will deselect that carrier.

>4/9/19, Harry Dunham:
Implementation of the JSON file reader/writer and an actual submission button
function. Additionally, the status button was replaced by a progressbar,
which isn't as practical when considering that this project modifies a local file,
however it is a mockup of the application should it ever have an actual
website backend and server support.
