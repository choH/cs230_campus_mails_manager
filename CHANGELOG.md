# CHANGELOG

> This file serves as the journal for the [campus_mails_manager](https://github.com/cs230s19/campus_mails_manager) project.

---

## Broadcasts

### 2019-04-10 | Final scrum meeting (17:00 @Andrews)
* Everyone should have his parts done by the time of meeting, so that the team can get together, merge three screens into one program and run some test trials.
* The team should polish this `CHANGELOG.md` file and update the [`README.md`](https://github.com/cs230s19/campus_mails_manager/blob/master/README.md).

### 2019-04-10 | Change on `registered.data`.

* Values of `tracking_num`, `box_num`, `bin_num` are now in `string` type.
    * I apologize for editing the most fundamental file at this stage, but I believe by having all values store as `string` would simplify the searching implementation (avoid type-check during looping). Also it is more consistent with the nature of all input features, as `TextInput.text` is default to be `string`.
* Key `service` is now `carrier` for better description.
* Key `delivered_time` is now `registered_time` for better description, consistency with `registered_staff`, and not to be confused with the delivery time of the carrier if we will ever do the bar code stuff.
* `is_redeemed` is now `redeemed_status`. Also, rather than having a boolean value, `redeemed_status` now has alternative values of `"Redeemed"` or `"Unredeemed"` — this make the display output much easier.

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

### 2019-04-10
* Tried to access widget attributes from another screen in python, mostly failed. Thus we simplify the design for `Details Screen` with a bypass button on `Log Screen`.
* Merged all three screens together.
* Adopted the design of having three screen-shift buttons in the bottom bar.

### 2019-04-09
* Achieved demo UI for all three screens.
* The task of interacting with JSON must be postponed due to unforeseen amount of work. 
* Discuss the possibility of editing `registered.data`.

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

### 2019-04-12, Henry Zhong:
* **Updated [`README.md`](https://github.com/cs230s19/campus_mails_manager/blob/master/README.md) for Class Presentation**
    * Purpose of this project
    * UI Showcase & User Manual.
    * Vision for future possibilities.
    * Acknowledgements.

### 2019-04-11, Henry Zhong:
**The Program is Functional for Demo Trails and Presentation**
* Merged the actual `Input Screen` and `Details Screen` into the framework.
* Finished some small adjustments on `Input Screen` code to be compatible with the recently the updated `registered.data` file and screen-jump bottom bar buttons.

### 2019-04-10, Nathan Devereux:
* **Fully implemented Details Screen.**
    * Added a button in the Log Screen that calls the function to get the details of a specific package. 

### 2019-04-10, Henry Zhong:
**`LogScreen` is now fully functional**
* **JSON Interaction Implemented**
    * Being able to obtain JSON entries with generator, specifically:
        * Entries which with matched keys/values to the `search_dict`.
        * Entries with matched value to the unspecified `search_input`.
        * All entries.
* **Search Function Fully Implemented**
    * Color-coding implemented: including situation of select, deselect, and over-ruling select (selected a filter but did not submit an input, then selected another filter, the pervious filter will be deselect automatically).
    * Implemented wrapper functions to generate `search_dict` base on user input, thus the program can use such dictionary to interact with JSON.
    * Implemented some user friendly features:
        * Auto search input text cleaning once `Submit`.
        * Dynamic hint display on search bar once a filter is selected.
* **Reset Button Implemented**
    * Reset everything user input (filters etc.) on this screen.
* **Canceled Spinner for `Carrier` and `Redeem Status`**
    * Due to the limitation of time, the spinner implementation for `Carrier` and `Redeem Status` have been canceled.
    * User may still use text input + hint text to search on these two keys.
    * As the `LogScreen` is now solely interacting with users on text input, the implementation of search logic became easier.
* **Screen Jump Feature Experimented**
    * Made two mimic screens for `InputScreen` and `DetailsScreen`, able to jump over three screen with intuitive transition directions.
    * Migrated codes from `log.py` and `log.kv` to `manager.py` and `manager.kv` for the seek of cross screen interaction.


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

