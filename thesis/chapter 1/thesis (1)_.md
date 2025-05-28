

# introduction:



## The first generation (1G) :

The first cellular phone networks were analog, it was the first generation.   generation.The first wireless terminals, the analog radiotelephones, were installed   in cars or carried in briefcases.They were huge, consumed a lot   of energy and having limited coverage.1G offered a mediocre and very expensive service.   of mobile communication.1G had many flaws, such as the standards   incompatible from one region to another, an unsecured analog transmission (listening to   the calls).The first generation of cellular telephony was deployed under the name   commercial AMPS (Advanced Mobile Phone Service) and used frequency division multiplexing   (FDMA) to carry voice channels in the 800 MHz band.   This first generation of cellular networks using analog technology was   replaced as soon as a more efficient second generation using a   digital technology.[6][gsm7]

## The second generation (2G):

The GSM network is a standard of mobile telephony known as "second generation."   (2G), unlike the first generation, communications operate in an   fully digital mode.   The GSM standard allows a rate of 9.6Kbits/s, which enables the transmission of voice and thus   only low-volume digital data.2G enabled the development and the   launch of the SMS (Short Message Service) accessible to GSM subscribers.It is about   a text message transmission service with a content limit of 160 characters.   Among the advantages of the second generation, we can mention: better sound quality,   portable devices and a certain level of communication privacy.The advancements of the   second generation allowed the general public access to mobile telephony [7][gsm7]

# Architecture of a GSM network :

## Mobile Station :

The Mobile Station consisting of the physical terminal contains the radio transceiver, the display and digital signal processors and the Subscriber Identity Module (SIM). the SIM pro'ides the user with the ability to access his subscribed services irrespective of the location and the terminal used. The insertion of the SIM in any GSM cellular phone allows the user to access a network, give and receivephone calls and make use of all the subscribed services.[book10]

The International Mobile Equipment Identity (IMEl) uniquely identifies the mobile 
terminal according to the International Mobile Subscriber Identity ( IMS I) contained in 
the SIM. Because the IMEl and IMSI are independent. personal mobility is possible. The 
SIM can he protected against unauthorised use by a personal identity number (PIN).[book10]

The Mobile Station: The mobile station in GSM is really two distinct entities. It consists of the mobile equipment, i.e the handset, and a smart card called the Subscriber Identity Module (SIM). The SIM provides personal mobility, so that the user can have access to subscribed service irrespective of a specific terminal. By inserting the SIM card into another GSM terminal. The user is able to receive and make calls from that terminal, and receive other subscribed service. The mobile equipment is uniquely identified by the International Mobile Equipment Identity (IMEI). The SIM card contains the International Mobile Subscriber Identity (IMSI) used to identify the subscriber to the system, a secret key for authentication and other information. The IMEI and IMSI are independent, thereby allowing personal mobility. The SIM card may be protected against unauthorized use by a password or personal identity number.[article 04]

## Base station subsystem:

The Base Station Subsystem is composed of two parts the Base Transceiver Station BTS and the Base Station Controller BSC These communicate across the standardized Abis interface allowing as in the rest of the systemoperation between components made by different suppliers.[book05]

### Base Transceiver Station BTS:

The Base Transceiver Station houses the radio transmitters that dene a cell and handles the radiolink protocols with the Mobile Station. In a large urban area, there will potentially be a large number of BTSs deployed thus, the requirements for a BTS are ruggedness, reliability, portability, and minimum cost [10]

### Base StationController BSC :

The Base Station Controller (BSC): management of one or more base stations and communication with them via the A-bis interface. This controller performs various tasks related to communication and operation. The BSC acts as a concentrator for the communication functions of signals coming from the base stations, as it transfers communications from different base stations to a single output. In the opposite direction, the controller transmits data to the appropriate base station. The BSC supplies the database of the base stations and serves as a relay for various alarm signals intended for the operations and maintenance center. The management of radio resources for the area covered by the different connected base stations is another important function. This allows the controller to manage intercellular transfers of users within its coverage area, that is, when a user moves from one cell to another Mobile communication passes from one cell to another.[gsm5]

### Network Switching Subsystem (NSS):

The NSS main role is to manage the communications between GSM and other network users. Another task of it includes the main switching functions of GSM, databases required for the subscribers, and mobility management.

### Mobile Station Controller (MSC):

The interface A connects the mobile switching center to the radio subsystem. Its main role is to ensure switching between the subscribers of the mobile network and those of the public switched network (RTC), or its digital equivalent, the ISDN network. It provides various services to subscribers, such as telephony, value-added services, and messaging services. It is also possible to update the various databases (HLR and VLR) that contain all the data concerning subscribers and their location within the network. The MSC switches of an operator are connected to each other for internal information switching. To ensure interoperability between operators' networks, MSCs serving as gateways (Gateway Mobile Switching Center, GMSC) are placed on the periphery of an operator's network.[gsm5]

### The authentication center (AUC):

The authentication center (AUC) provides authentication and encryption parameters that verify the user's identity and ensure the confidentiality of each call. The AUC protects network operators from different types of fraud found in today's cellular 
world. The GSM has standard encryption and authentication algorithm which are used to dynamically compute challenge keys and encryptions keys for a call.[book06]

### The equipment identity register (EIR):

The equipment identity register (EIR) is a database that contains information about the identity of mobile equipment that  prevents calls from stolen, unauthorized, or defective mobile stations. The AUC and EIR can be implemented as stand-alone  nodes or as a combined AUC/EIR node.[book06]

### Home Location Register(HLR):

This database contains all the regulatory data about every supporter alongside their last known area. Along these lines, theGSM system can course calls to the applicable base station for the MS. At the point when a client switches on their telephone, the telephone registers with the system and from this it is conceivable to figure out which BTS it speaks with so approaching calls can be steered suitably. Notwithstanding when the telephone is not dynamic (but rather exchanged on) it re-enrolls
 intermittently to guarantee that the system (HLR) knows about its most recent position. There is one HLR per organize, despite the fact that it might be dispersed
 crosswise over different sub-focuses to for operational reasons.[article03]

### Visitor Location Register(VLR):

 The VLR is a database that contains the temporary abonné information that the
MSC needs to keep track of the abonnés while they are visiting. The MSC and
the VLR are always connected. When a mobile station moves to a new MSC
zone, the VLR connected to that MSC will ask the HLR for information on the
station. The VLR will provide the information required to set up the call without
having to ask the HLR each time if the mobile station sends out an appeal later.

### Gateway Mobile Switching Center (GMSC):

 The GMSC is the indicate which a ME ending call is at first steered, with no information of the MS's area. The GMSC is hence responsible for acquiring the MSRN (Mobile Station Roaming Number) from the HLR in light of the MSISDN (Mobile Station ISDN number, the "index number" of a MS) and steering the call to the right went to MSC. The "MSC" part of the term GMSC is misdirecting, since the passage operation does not
 require any connecting to a MSC.[article03]

### SMS Gateway (SMS-G):

 The SMS-G or SMS door is the term that is utilized to all things considered portray the two Short Message Services Gateways characterized in the GSM measures. The two portals handle messages coordinated in various bearings. The SMS-GMSC (Short Message Service Gateway Mobile Switching Center) is for short messages being sent to a ME. The SMS-IWMSC (Short Message Service InterWorking Mobile Switching Center) is utilized for short messages started with a portable on that system. The SMS-GMSC part is like that of the GMSC, while the SMS-IWMSC gives a settled get to indicate the Short Message Service Center.[article03]

## Operation Support Subsystem (OSS):

The operations and maintenance center (OMC) is connected to all equipment in the switching system and to the BSC. The implementation of OMC is called the operation support system (OSS). The OMC provides a single point for the maintenance personnel to maintain the entire system.[article01]

## GPRS (General Packet Radio Service) 2.5G:

 As the requirement for sending data on the air-interface increased, new elements such as SGSN (Serving GPRS) and GGSN (Gateway GPRS) were added to the existing GSM system. These elements made it possible to send packet data on the air-interface. This part of the network handling the packet data is also called the 'packet core network'. In addition to the SGSN and GGSN, it also contains the IP routers, firewall servers and DNS (domain name servers). This enables wireless access to the Internet and the bit rate reaching to 150 kbps in optimum conditions.[book12]

## EDGE (Enhanced Data Rates for GSM Evolution) 2.75G:

 The EDGE standard is a mobile telephony standard, an evolution of GSM. This technology adopts a new modulation allowing for higher data rates while using the existing GSM radio spectrum of the operators. Although with limited speeds compared to the UMTS (Universal Mobile Telecommunications System) technologies that follow, EDGE has the capability to offer almost all 3G services. it therefore constitutes an interesting solution for an operator who wishes to offer 3G services using the already existing spectral resources of 2G.[book12]

# The third  generation (3G):

In EDGE, high-volume movement of data was possible, but still the packet transfer on
the air-interface behaves like a circuit switch call. Thus part of this packet connection
efficiency is lost in the circuit switch environment. Moreover, the standards for developing the networks were different for different parts of the world. Hence, it was decided to have a network that provides services independent of the technology platform and whose network design standards are same globally.[book 12]

## User Uquipement (UE):

## Universale Mobile Telecommunications Syste UMTS:

UMTS is regarded as a third generation (3G) wireless communication system that acts
as a successor to the second generation (2G) communication technologies and is an evolved version of GSM GPRS and EDGE (Poole, 2006). The GSM network was used to provide voice capabilities to subscribers but they was need to support the increasing number of subscribers while providing high speed data services. The Third Generation Partnership Programme (3GPP) was formed to oversee the implementation of a system that could offer support to those services.[art-gsm]

## Universal Terrestrial Radio Access Network (UTRAN):

The UTRAN is the part of the UMTS network that is of highest concern in this thesis
work, therefore it will be described in details.

## Node-B :

The NodeB is equivalent to the BTS of the GSM network. It can
manage one or more cells. It includes a CDMA receiver that converts signals
from the Uu interface or Air interface into data streams routed to the RNC on

the Iub interface. In the other direction, the CDMA transmitter converts the
data streams received from the RNC for transmission over the air interface.
 [17]

## Radio Access Network (RAN):

The main elements in this part of the network are the base station (BS) and the radio
network controller (RNC). The major functions include management of the radio resources and telecommunication management.[BOOK 12]

## Radio Network Controller (RNC) :

The Radio Network Controller is responsible for controlling and switching resources in UTRAN. It is connected to Iub and Iu interfaces. Several RNCs can be connected together with an inter-RNS connection called the Iur interface.

[TEKNIIKAN JA LIIKENTEEN TOIMIALA]

## Core Network (CN):



![](C:\Users\Blue%20Info%2038\AppData\Roaming\marktext\images\2025-05-20-20-39-12-image.png)

## LONG TERM EVOLUTION (LTE):

Long Term Evolution (LTE) is a fourth generation wireless communication standard developed by the 3GPP (Setiawan and Ochi, 2009), although the standard was first publish in 2005 by the 3GPP in its release 6 (Mustaqim et al., 2012) it has been under development and was fully published in 2008 in the release 8 documentation of the 3GPP. The LTE is often referred to as 4G but the LTE-Advanced which was defined in the release 10 is considered as the true 4G network and release 8 is considered as 3.9G. LTE was implemented as a solution to solve the high demand for data rates by services such as gaming, streaming and web browsing which have increased the data rates from Mbit/s to Gbit/s. Another reason for the implementation of LTE was to reduce delay and latency in network services while increasing the spectral efficiency of the network.[art 3G 03]



`Lo`ng Term Evolution ou LTE est une évolution des normes de téléphonies mobile , l’une des  grandes spécifications de ce réseau est l’utilisation de la technique de codage OFDMA sur la voie  descendante et le SC-FDMA pour la voie montante, ce qui va permettre à chaque cellule de disposer  d’une largeur spectral de plus de 3 à 20 MHz et du coup d’avoir une bande passante plus importante  et ainsi augmenter le débit. Le réseau LTE dispose d’une architecture assez simplifiée, elle est  constitué de deux parties : Une partie Radio ou eUTRAN et un réseau cœur EPC (Evolved Packet Core) [gsm]

### .1 E-UTRAN:



## User equipment (EU):

The internal architecture of LTE user equipment is identical to that used by UMTS and GSM, which is actually a mobile device (ME) that handles all communication functions. It is also known as the SIM card.[gsm7]

## Evolved Packet Core(EPC):

The core network called “EPC” uses “full IP” technologies, that is based on Internet protocols for signaling which allows reduced latency times, voice and data transport. This network core allows interconnection via routers with other remote eNodeB, networks of other mobile operators, fixed telephony networks and the Internet.
EPC simplifies the network architecture to any IP, as it ensures mobility between 3GPP radio access, and also not 3GPP for example WIMAX and CDMA2000.

## Home Subscriber Server (HSS):

##  hosts database that contains the user subscription data of the EPS. It provides user authentication and access authorization, also has the identity of MME to which a user is attached or registered. In addition, HSS holds the information about the PDNs that the user can connect. It is based on the Home Location Register (HLR) and Authentication Centre (AuC).[Master_Thesis_Jose_Gamboa]

## Mobility Management Entity (MME):

The MME is the control node that manages signaling between the EU and the core network. He is responsible for managing the links between an UE and a logical node of the core network, including the establishment, reconfiguration and release phases of these links. One of its major roles is to manage the signaling and security connection between the network and the EU.[18][19][20][gsmfr]

## Serving Gateway (SGW) :

All IP packets to a user are transferred through the SGW. If the SGW receives data for a standby EU, it contacts the MME to notify the EU and thus restore the links associated with the contexts. It also performs some ancillary functions within the visited network in the roaming context, such as sending billing information (for example, the volume of data sent and received by the user).[18][19][20][gsmfr]

## P-GW (Packet GetWay):

Provides data connectivity to external packet data networks such as the Internet or IP Multimedia Subsystem (IMS). IMS networks are used to provide multimedia services such as voice over Internet protocol (VoIP), video conferencing and messaging.[gsm3]

### eNodeB:

eNodeB is the equivalent of BTS in the GSM network and NodeB in the UMTS network. The transfer functionality is more efficient in LTE. These are antennas that use RF air interfaces to connect the UEs to the core network of the LTE. In addition, eNodeB has the capability of radio controller, which means that the result is more efficient and the network is less latent. For example, eNodeB determines mobility 
instead of BSC or RNC.[gsm5]

### X2 interface:

It is a logical interface, it is introduced in order to allow eNodeBs 
to exchange signaling information during handover or signaling, without involving the core network. 
When the user moves in ACTIVE mode (Handover) from one eNodeB to another eNodeB, new resources are allocated on the new eNodeB for the EU; however, the network continues to transmit its data to the old eNodeB until it has been informed of the change. 
In order to minimise the loss of its data packets, the old eNodeB relays incoming packets on the X2 interface to the new eNodeB which delivers them to the EU. 
The eNodeB is connected to the core of the network through the S1 interface.[gsm6]

### Interface S1 :

It is the interface between eNodeB and MME and S-GW. At the user level, this interface will be based on the user data tunnel (GTP-U) (similar to the Iu and Gn interfaces of 3G). In the control plane, the interface is more similar to the application part of the radio access network, with some simplifications and modifications due to the different distribution of functions and mobility within the EPS.[gsm3]



















[3] M.A. Rakotomalala, « Evolution des réseaux mobiles », Cours M2-STI-TCO-ESPA, Année Universitaire 2016-2017.

[2]:BOUGUEN, Yannick, HARDOUIN, Eric, et WOLFF, François-Xavier. LTE pour les
reseaux 4G. Editions Eyrolles, 2012. 

6] Jean-Marie Dilhac « Une introduction aux télécommunications », Presses Universitaires du Mirail, 04/10/2012.
[7] JOACHIM Tisal, “Le réseau GSM: l’évolution GPRS, une étape vers l’UMTS”, edition 3,
1999 

[17]POUR, DEVELOPPEMENT D’UNE APPLICATION MOBILE.
"MEMOIRE DE FIN D’ETUDES en vue de l’obtention du DIPLOME de
Master."

[10]Scourias, John. "Overview of the global system for mobile
communications." University of Waterloo 4 (1995).

[18]M. Rumney, « LTE and the Evolution to 4G Wireless », Agilent Technology, 2009 
[19]E. Dahlman, S. Parkvall, J. Sköld, P. Beming, « 3G Evolution HSPA and LTE for Mobile 
Broadband », Second Edition Academic Press, 2008 
[20]E. Dahlman, S. Parkvall, J. Sköld, « 4G LTE / LTE – Advanced for Mobile Broadband », 
Academic Press, 2011
