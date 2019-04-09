# CHANGELOG

> This file serves as the journal for the [campus_mails_manager](https://github.com/cs230s19/campus_mails_manager) project.

---

## Broadcasts

### 2019-04-09 | Scrum meeting after class.
Everyone are expected to have a screen with fully functional UI and be able to interact with the `registered.data` by the meeting.

### 2019-04-07 | A short style guide for updating this `CHANGELOG.md`.
* The `CHANGELOG.md` has three sections.
    * **Broadcasts**: Briefing of upcoming events or reminders (like this one).
    * **Scrum Meetings**: Summaries for scrum meetings.
    * **Development Journal**: Records for development updates.
* For the sake of consistency, I suggest we update this `CHANGELOG.md` in a date descending order (new-to-old) with a format of `YYYY-MM-DD`.



---
## Scrum Meetings

### 2019-04-06
* Sketched and discussed the UI design for each screens.
* Emphasized the necessary buttons to navigate between screens.
    * `Input Screen` <-- `Submit Button` within bottom bar --> `Log Screen`
    * `Log Screen` -- `Edit Button` within each entries --> `Details Screen`
    * `Details Screen` -- `Back Button` --> `Log Screen`
* Specified duties of each `Screen`.
    * `Input Screen`
        * Collects info about the delivery and injects them into `registered.data`.
        * A visual cue indicating successful add of delivery entry.
    * `Log Screen`
        * Filters for entries.
        * Sorting options for entries.
        * A scrollable section to display registered entries from `registered.data`
    * `Details Screen`
        * Display the details of selected entry base on `registered.data`.
        * Edit the selected entry.
        * A `Back Button`.
        
### 2019-04-04
* Created [GitHub repo](https://github.com/cs230s19/campus_mails_manager) with necessary files.
* Updated the [`registered.data`](https://github.com/cs230s19/campus_mails_manager/blob/master/registered.data) with test trials in `JSON` format.

### 2019-04-02
* Discussed the general picture of the project, with screens distributed.
    * Harry: `Input Screen`
    * Henry: `Log Screen`
    * Nathan: `Details Screen`
* Set the output resolution to be a mimic of iPhone XS, as for `2436 * 1125`.

 
 
---
## Development Journal

### 2019-04-09, Harry Dunham:
* **JSON Read/Write and Popups.**
    * Implementation of the JSON file reader/writer and an actual submission button function.
    * Additionally, the status button was replaced by a progressbar, it is a mockup of the application should it ever have an actual website backend and server support.
    * A basic popup system was added for failing to fill out specific text fields.

### 2019-04-08, Harry Dunham:
* **Mail Carrier Implementation.**
    * Fixed the carrier implementation so that whenever one carrier is selected all the other carriers are deselected. 
    * Additionally if the user selects the currently selected carrier it will deselect that carrier.

### 2019-04-07, Henry Zhong:

* **Demo Layout Implemented.**
    * Implemented a demo layout for search bar, filter buttons/spinners, and dynamically-added widgets within scrollview.

### 2019-04-06, Harry Dunham:

* **Abstract Implementation of the Input Screen.** 
    * This includes basic text inputs and a non-functioning submit button (inputs include: tracking number, current date, bin number, etc.) 
    * This is meant to get a visual understanding of what the input screen should look like.
