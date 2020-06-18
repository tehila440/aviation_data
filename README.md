#### Investigating Airplane Accidents

This data set contains 77,282 aviation accidents that occurred in the United States.  The data in `AviationData.txt`
comes from the [National Transportation Safety Board (NTSB)](https://www.ntsb.gov/Pages/default.aspx).

Each row contains data about a single aviation accident. Here are descriptions for some of the columns:

* `Event Id` - The unique id for the incident
* `Investigation Type` - The type of investigation the NTSB conducted
* `Event Date` - The date of the accident
* `Location` - Where the accident occurred
* `Country` - The country where the accident occurred
* `Latitude` - The latitude where the accident occurred
* `Longitude` - The longitude where the accident occurred
* `Injury Severity` - The severity of any injuries
* `Aircraft Damage` - The extent of the damage to the aircraft
* `Aircraft Category` - The type of aircraft
* `Make` - The make of the aircraft
* `Model` - The model of the aircraft
* `Number of Engines` - The number of engines on the plane
* `Air Carrier` - The carrier operating the aircraft
* `Total Fatal Injuries` - The number of fatal injuries
* `Total Serious Injuries` - The number of serious injuries
* `Total Minor Injuries` - The number of minor injuries
* `Total Uninjured` - The number of people who did not sustain injuries
* `Broad Phase of Flight` - The phase of flight during which the accident occurred
* `Weather Condition` - The basic weather conditions at the time of the event. [VMC](https://en.wikipedia.org/wiki/Visual_meteorological_conditions),
[IMC](https://en.wikipedia.org/wiki/Instrument_meteorological_conditions), or UNKNOWN

The first part of this project is a guided project from DataQuest and the goal is to explore different
techniques for searching for values.

Task 1
* Count how many accidents occurred in each U.S. state
* Determine which state had the most accidents overall
Top three states were California, Florida, Texas.  California had the most accidents, 8030.

Task 2
* Count how many fatalities and serious injuries occurred during each month
Noember 1996 had the highest total injuries (fatalities + serious) with 1022.

Task 3
* Count the number of accidents by air carrier.
* Count the number of accidents by airplane make and model.
* Figure out what percentage of accidents occur under adverse weather conditions

United Airlines had the most accidents.  The Cessna 152 was the make & model with the most accidents.
Only 7.2% of the accidents occured under adverse weather conditions.

