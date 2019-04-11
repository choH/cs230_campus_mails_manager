# campus-mails-manager
> To digitalize College of Wooster's mailing workflow. 

---
A proper `README.md` file will be written once the program is fully developed. During the development stage, the records will be update on [`CHANGELOG.md`](https://github.com/cs230s19/campus_mails_manager/blob/master/CHANGELOG.md).


---
## Purpose of This Project
The purpose of this project is to digitalize College of Wooster's mailing — mostly regarding delivery archiving, notifying, and redeeming aspects — workflow. 

In shorts, rather than having the mailing room staffs manually sort the deliveries, fill out the blue slip, put it in your mail box, have you to go and redeem it, then keep the redeemed blue slip for another month... We aim to design an app for these mailing room staff so that they can input information digitally (even though a scan), the recipient shall automatically sent notification email, and you can present such email to redeem your package.

## UI Showcase & User Manual.

![UI Demo](https://github.com/cs230s19/campus_mails_manager/blob/master/ui_demo.png)

* **Input Screen**
    * This screen is the default screen of the application, so the staff may quickly access it and input information regarding the just arrived package.

* **Log Screen**
    * This screen is display all registered packages implemented with filters, so the staff may quickly find the desired log of the package if requested.
    
* **Details Screen**
    * This screen show all information regarding a specific package entry.


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
