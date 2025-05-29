## Introduction:

The 2G GSM (Global System for Mobile Communications) technology is one of the major second-generation mobile network technologies. It brought significant improvements over the previous technology (AMPS), including digital modulation, circuit switching, and time division multiplexing. GSM allowed data transmission rates of up to 9.6 Kbps and introduced security features such as encryption to protect communication. GSM is a European 2G standard. Its commercial development started in 1991, becoming popular worldwide. The first system to be used had an operating frequency of 900MHz, with future variants in 1800MHz, 1900MHz, and 450MHz.

## 1-Architecture of a GSM network :

The GSM network is divided into three main subsystems which are Base Station Sub-system *(BSS)*, Network Sub-system *(NSS)* and Operation Support Sub-system *(OSS)*. The overall structure of the GSM network, encompassing the three subsystems along with the various interconnections among them and the internal connections within the distinct components of each subsystem, is presented in **Figure 1.1**.

![](https://media.geeksforgeeks.org/wp-content/uploads/network-GSM.jpg)

`https://media.geeksforgeeks.org/wp-content/uploads/network-GSM.jpg`

### Mobile station:

The mobile station is the device used by the user, such as a mobile phone. It consists of a mobile equipment *(ME)* and a Subscriber Identity Module (SIM) card. The ME is the hardware of the mobile phone, while the SIM card contains subscriber identification information.

## Base station subsystem *(BSS)*

The Base Station Subsystem provides the radio access and handles communication between the mobile phone *(Mobile Station or MS)* and the rest of the network. The **BSS** composed of two parts, the Base Transceiver Station *(BTS)* and the Base Station Controller *(BSC)*, that communicates across the standardized **A-bis** interface.

![image (2).png](assets/9eb4afe6d051e98f645e4585550fd14fd8b5dbb6.png)

`**Figure**: 2G GSM architecture [^ Analysis of 2G and 4G Network Quality in Solok City]`

### Base Transceiver Station *(BTS)*

The **BTS** is responsible for providing coverage and connectivity to mobile devices within it's service area. It contains transmitter and receiver equipment that transmit and receive radio signals to the mobile station, as well as a few components for signal and protocol processing *(error correction coding, modulation, equalization)*.

### Base Station Controller *(BSC)*:

The base station controller is responsible for the management and control of base stations in a particular area. The **BSC** manages a group of **BTS's** via an **A-bis** interface. It handles functions such as radio channel allocation, handover management between cells, and power control. It is also a switch that carries out a concentration of circuits towards the **MSC** via an **A-interface**.

## Network Switching Subsystem (NSS):

It is a fixed network that includes all the functions necessary for establishing calls and mobility. It includes switches, gateways to the PSTN (Public Switched Telephone Network) as well as databases.

### The Mobile service Switching Centre (MSC)

The mobile switching center is responsible for call switching, mobility management over the radio network and other networks, radio resource management hand over between **BSC**, billing information. The MSC is also connected to other networks, such as the fixed telephone network, for call routing. Calls originating from or terminating in the fixed network are handled by a dedicated Gateway **MSC** *(GMSC)*. A cellular network can have several **MSC's** with each being responsible for a part of the network. 

### Gateway Mobile Switching Center (GMSC):

The mobile gateway switching center is a device which roots traffic entering a mobile network to the correct destination. The gateway mobile switching center is responsible for the interconnection between the GSM network and other networks, such as fixed networks or mobile networks of other operators.

### Home location register (HLR)

The **HLR** is a database that manages subscribers of a **PLMN** *(Public Land Mobile Network)*. It stores details of all subscribers in the network such as subscription information, location information, the subscriber's international identity used by the network *(IMSI)*, the subscriber's directory number *(MSISDN)*, and the subscription profile. A subscriber is therefore associated with a unique **HLR**, regardless of their location, and is then identified by their **MSISDN**.

### Visitor Location Register (VLR)

The **VLR** is a database that stores data temporarily for mobile served by the **MSC** *(each **MSC** has a **VLR**)*, information stored includes: **IMSI**, mobile station **ISDN** number, mobile station roaming number, temporarily mobile station identity **TMSI**, local mobile station identity, the location area where the mobile station has been registered, and supplementary service parameters.

### The Equipment Identities Register (EIR):

Is a database that contains the International Mobile Equipment Identity Number *(IMEI)*. This database list's mobile terminals.

### The authentication center (AUC):

This database enables the authentication of service requests and the encryption of communications using appropriate algorithms. The **AUC** communicates with: **HLR**, **MS's** **SIM** card *(which contains the **IMSI**)*, and the **BTS** *(which contains an encryption algorithm)*.

### Operation Support Subsystem (OSS):

It ensures the management and supervision of the network. Network supervision occurs at many levels: fault detection, site commissioning, parameter modification, and statistics production.

## GPRS (General Packet Radio Service) 2.5G:

The growing demand on data services require the integration of new elements such as **SGSN** *(Service **GPRS**)* and GGSN (GPRS Gateway) to the existing GSM system by introducing a device on the **BSC** called a PCU (Packet Controller) that manages packet data transmission. Which contributes to connecting the GSM network to the Internet and ensuring data transmission. The maximum speed reached was 114 kbps.

---

### EDGE (Enhanced Data Rates for GSM Evolution) 2.75G:

The **EDGE** standard is a mobile telephony standard, an evolution of **GSM**. This technology adopts a new modulation allowing for higher data rates while using the existing **GSM** radio spectrum of the operators. It is characterized by better speed and performance compared to **GPRS**, about 384kbps.Although with limited speeds compared to the UMTS (Universal Mobile Telecommunications System) technologies that follow, EDGE has the capability to offer almost all 3G services. it therefore constitutes an interesting solution for an operator who wishes to offer 3G services using the already existing spectral resources of 2G.

### Operation mode

When the mobile device is powered on, the following operations occur:

- The user activates their SIM card.

- The GSM receiver scans the channels in the GSM band and measures the signal strength on each channel.

- The mobile identifies the BCCH (Broadcast Control Channel) among the strongest signals.

- The mobile retrieves the information related to the FCCH (Frequency Correction Channel), which helps it precisely align with GSM channels.

- The mobile receives the synchronization signal of the TDMA frame transmitted on the BCCH and synchronizes its frame accordingly.

- The mobile reads information from the BCCH regarding the cell and the network and sends the caller's identification to the BTS (Base Transceiver Station) for location updating.

Once this startup phase is completed, the mobile enters standby mode, during which it performs routine tasks such as:

- Reading the PCH (Paging Channel) to detect possible incoming calls.

- Reading the signaling channels of neighboring cells.

- Measuring the BCH (Broadcast Channel) levels of neighboring cells in preparation for a potential handover.

When Receiving a Call:

- A landline user dials the mobile subscriber's number: 06 XX XX XX XX.

- The call is routed to the nearest MSC (Mobile Switching Center), which searches the IMSI in the HLR (Home Location Register) and the mobile's location in the VLR (Visitor Location Register).

- The MSC closest to the mobile (Visited MSC) broadcasts a message within the location area (covering several cells) to alert the targeted mobile via the PCH.

- The mobile responds on the RACH (Random Access Channel) with a Timing Advance set to 0 and a power level determined by the network (these parameters will be adjusted later).

- The network grants access through the AGCH (Access Grant Channel) and assigns the mobile a frequency and a time slot.

- The called subscriber is identified via the SIM card.

- The mobile receives the ringing command.

- The subscriber answers the call, and the communication is established.

When Making a Call:

- The mobile subscriber dials the number of the correspondent in the switched telephone network.

- The request reaches the BTS of its cell.

- It passes through the BSC (Base Station Controller) to reach the MSC.

- The caller is identified and their service rights are verified.

- The call is routed to the public network.

- The BSC requests the allocation of a channel for the upcoming communication.

- The recipient picks up, and the communication is established.











### The third generation (3G):

### Universale Mobile Telecommunications Syste UMTS:

### niversal Terrestrial Radio Access Network (UTRAN):

### 4-1 User Uquipement (UE):

### Node-B :

### Radio Access Network (RAN):

### Radio Network Controller (RNC) :

### Core Network (CN):

### 5- LONG TERM EVOLUTION (LTE):

## User equipment (EU):

## 5-2 E-UTRAN:

## 5-2-1 eNodeB:

## 5-3 Evolved Packet Core(EPC):

## 5-3-1 Home Subscriber Server (HSS):

## 5-3-2 Mobility Management Entity (MME):

## 5-3-3 Serving Gateway (SGW) :

## 5-3-4 P-GW (Packet GetWay):

## 5-3-5 Policy and Charging Rules Functin (PCRF):

## The interfaces of 4G lte :

The interfaces mentioned below are based on the Diameter protocol.

**The S6a interface*** establishes a connection between the MME and the HSS, facilitating the transfer of authentication and location data. This allows determining whether a user can access the LTE network.

**The S11 interface** ensures the link between the MME and the SGW, limited to signaling exchange.

**The S10 interface** connects two MMEs, allowing MME reinstallation as well as information transfer from one MME to another.

***The S3 interface*** connects the SGSN to the MME, enabling the exchange of information related to the user and the bearer, facilitating mobility within the 3GPP access network, whether in inactive or active state.

**The S1-MME interface** connects the eNode B to the MME, dedicated exclusively to signaling.

**The S5 interface** connects the PGW to the SGW, transporting user data as well as some signaling messages.

The S4 interface establishes a connection between the SGSN and the PGW, providing appropriate control.

The related interface serves as a mobility support between the GPRS core and the 3GPP anchoring function of the PGW.

The S1-U interface establishes a connection between the eNode B and the SGW, dedicated exclusively to the transport of user data, without signaling exchanges.

**The S1-MME interface*** connects the eNode B to the MME, limited to the transport of signaling messages.

**The X2 interface** interconnects two eNode B, allowing the transport of both user data and signaling messages.

**The Uu interface** or radio interface, ensures transmission over the radio channel and is located between the terminal (UE) and the eNode B, transporting both user data and signaling messages.

**The Gx interface** connects the PGW to the PCRF, allowing the PGW to access the charging rules provided by the PCRF, which enables it to and bill the user based on service flows rather than volume.

**The Rx interface** connects the PCRF to IP networks, ensuring quality of service.
Management service with the PCRF entity.

***The SGi interface*** establishes the connection between the PGW and the external IP network (Internet).
