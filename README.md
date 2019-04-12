# campus-mails-manager
> To digitalize College of Wooster's mailing workflow.

---
A proper `README.md` file will be written once the program is fully developed. During the development stage, the records will be update on [`CHANGELOG.md`](https://github.com/cs230s19/campus_mails_manager/blob/master/CHANGELOG.md).


---
## Purpose of This Project
The purpose of this project is to digitalize College of Wooster's mailing workflow — mostly regarding delivery archiving, notifying, and redeeming aspects.

In shorts, rather than having the mailing room staffs manually sort the deliveries, fill out the blue slips, put them in the recipient's mail box, have the recipient to go and redeem it, then keep the redeemed blue slips for another month... We aim to design an app which can handle all above process digitally and in a more automated manner by providing features of:

* Digital registration of deliveries (even through a scan).
* Searchable database for registered deliveries.
* Automatic email notification to recipients.
* Redeem with QRcode.
* System generated logs.

## UI Showcase & User Manual.

![UI Demo](https://github.com/cs230s19/campus_mails_manager/blob/master/ui_demo.png)

* **Input Screen | Harry Dunham**
    * This screen is the default screen of the application, so the staff may quickly access it and input information regarding the just arrived package.

* **Log Screen | Henry Zhong**
    * This screen is to display all registered packages with filters available, so the staff may quickly find the desired log of the package if requested.

* **Details Screen | Nathan Devereux**
    * This screen is to show all information regarding a specific package entry, for the scenario of redeeming confirmation.



## Vision for Future Possibilities.

To actually this make program functional within the campus, we need a backend support which we don't know well enough yet. But in terms of the front end design, these are the future goals.

* **Input Screen**
    * Bar code scanner.
    * Time stamp `registered_time` input.
    * Profile for `staff_id`.

* **Log Screen**
    * More modular/customizable in terms of the information displayed for each entry
    * Embed `Spinner` or `DropDown List` for `carrier` and `redeemed_status`
    * Fuzzy match for searching.

* **Details Screen**
    * Better communication with other two screen.
    * Edit / Delete feature.
    * View multiple entries continuously (e.g. entries selected in `Details Container` from `Log Screen`)

## Acknowledgements.

* **Henry Zhong**
    * Responsible for developing `Log Screen`.
    * Responsible for designing the framework of the application.
    * Writing this document.

* **Harry Dunham**
    * Responsible for developing `Input Screen` with a fake progress bar.

* **Nathan Devereux**
    * Responsible for developing `Details Screen` and its linkage with `Log Screen`.
