## Operation mode

When the mobile device is powered on, the following operations occur:

**Power On & Initialization:**

- The user initializes their SIM.

- The mobile receiver scans for available frequencies of nearby Base Transceiver Stations and measures the signal strength on each frequency.

- Cell Selection & Synchronization

- The mobile identifies the Broadcast Control Channel (BCCH) among the strongest signals to get system information.

- The mobile retrieves the information related to the Frequency Correction Channel (FCCH) and synchronizes the frequency accordingly.

- The mobile receives the synchronization signal of the TDMA frame transmitted on the Synchronization Channel (SCH) and synchronizes its frame accordingly.

- Location Update

- The mobile reads information from the BCCH regarding the cell and the network and sends the caller's identification to the BTS (Base Transceiver Station) for location updating.



Once these steps are completed, the mobile enters standby mode, during which it performs routine tasks such as:

- Reading the Paging Channel (PCH) to detect possible incoming calls.

- Measuring the Broadcast Channel (BCH) levels of neighboring cells in preparation for a potential cell reselection.



**When Receiving a Call:**

- A landline user dials the mobile subscriber's number.

- The call is routed to the nearest Mobile Switching Center (MSC), which searches the IMSI in the Home Location Register (HLR) and the mobile's location in the Visitor Location Register (VLR).

- The MSC closest to the mobile (Visited MSC) broadcasts a paging message via paging channel (PCH) within the location area to alert the targeted mobile.

- The mobile responds on the Random-Access Channel (RACH).

- The network grants access through the Access Grant Channel (AGCH) and assigns the mobile a frequency and a time slot.

- The network assigns a Standalone Dedicated Control Channel SDCCH for authentication and call setup.

- Network sends call setup message to the mobile.

- The mobile receives a ringing alert.

- Once user picks up, the communication is established and a Traffic Channel (TCH) is assigned to the mobile

## When Making a Call:

- The mobile subscriber dials a number, so, call initiation process begins.

- Access Request 

- The mobile sends a channel request using Random Access Channel (RACH).

- The request reaches the BTS of its cell, then passed through the BSC to reach the MSC.

- Channel Assignment

- Network responds with assignment using Access Grant Channel (AGCH), then SDCCH.

- Called party is paged SDCCH, then PCH for paging the called mobile.

- When the called mobile starts ringing, the alert is sent back to the caller using SDCCH/TCH.

- Once the recipient picks up, the call is about to begin, a Traffic Channel (TCH) is assigned, and the communication is established.



# KPIs analysis

## Immediate Assignment Success Rate

Immediate assignment success rate indicates the success rate of the mobile accessing the signaling channel and affects the user experience.

**Recommended Formula:**

Immediate Assignment Success Rate = (Successful Immediate Assignments/Immediate Assignment Requests) x 100%

## TCH Assignment Success Rate

The TCH assignment success rate indicates the rate of the mobiles successfully seizing the TCHs to make calls. This KPI directly affects the user experience.

**Recommended Formula:**

TCH Assignment Success Rate = (Completed TCH Assignments/TCH Assignment Requests) x 100%

## TCH Congestion Rate

The TCH congestion rate is the proportion of the number of TCH assignment failures to the number of TCH seizure requests. If the TCH congestion rate is high, the network service quality deteriorates.

**Recommended Formula:**

TCH Congestion Rate = [Failed TCH Seizures due to Busy TCH / TCH Seizure Requests] x 100%







---

## SDCCH Call Drop Rate

The SDCCH call drop rate indicates the probability of call drops when the mobile occupies the SDCCH. If the value of this KPI is high, user experience is adversely affected.

**Recommended Formula:**

Call Drop Rate on SDCCH = (Call Drops on SDCCH/Successful SDCCH Seizures) x 100%

## Call Setup Success Rate *(CSSR)*

The Call Setup Success Rate (CSSR) indicates the probability of successful calls initiated by the mobile. If this KPI is too low, the subscribers are not likely to make calls successfully. The user experience is thus affected.

**Recommended Formula:**

CSSR = Immediate Assignment Success Rate x Assignment Success Rate x (1 – SDCCH Drop Rate) x 100%

---
