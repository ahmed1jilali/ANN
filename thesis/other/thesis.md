# introduction:

## The first generation (1G) :

The first cellular phone networks were analog, it was the first generation.   generation.The first wireless terminals, the analog radiotelephones, were installed   in cars or carried in briefcases.They were huge, consumed a lot   of energy and having limited coverage.1G offered a mediocre and very expensive service.   of mobile communication.1G had many flaws, such as the standards   incompatible from one region to another, an unsecured analog transmission (listening to   the calls).The first generation of cellular telephony was deployed under the name   commercial AMPS (Advanced Mobile Phone Service) and used frequency division multiplexing   (FDMA) to carry voice channels in the 800 MHz band.   This first generation of cellular networks using analog technology was   replaced as soon as a more efficient second generation using a   digital technology.[6][gsm7]

## The second generation (2G):

The GSM network is a standard of mobile telephony known as "second generation."   (2G), unlike the first generation, communications operate in an   fully digital mode.   The GSM standard allows a rate of 9.6Kbits/s, which enables the transmission of voice and thus   only low-volume digital data.2G enabled the development and the   launch of the SMS (Short Message Service) accessible to GSM subscribers.It is about   a text message transmission service with a content limit of 160 characters.   Among the advantages of the second generation, we can mention: better sound quality,   portable devices and a certain level of communication privacy.The advancements of the   second generation allowed the general public access to mobile telephony [7][gsm7]

# Architecture of a GSM network

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

L'élément central est la station de base, qui est un ensemble d'émetteur et de
récepteur qui pilote une ou plusieurs cellules. Dans le réseau GSM, chaque cellule principale au centre d'une station base peut être divisée en plus petites cellules qui sont des portions de la cellule de départ et utilisent des fréquences porteuses différentes grâce à des antennes directionnelles. La station de base sert de relais
entre le mobile et le sous-système réseau. Étant donné que le multiplexage temporel est limité à huit intervalles de temps, une station de base peut gérer jusqu'à huit connexions simultanément par cellule. Elle effectue les tâches de la couche liaison de données et de la couche physique.. En cas de besoin, on peut exploiter une station de base localement ou par télécommande à travers son contrôleur de station de base.[gsm5]

### Base StationController BSC :

Le contrôleur de station de base (BSC) : gestion d'une ou plusieurs stations de base et communication avec elles via l'interface A-bis. Ce contrôleur effectue diverses tâches au niveau de la communication et de l'exploitation. Le BSC agit comme un concentrateur pour les fonctions de communications des signaux en provenance des stations de base car il transfère les communications des différentes stations de base vers une sortie unique. Dans l'autre sens, le contrôleur transmet les données en direction de la station de base appropriée. Le BSC alimente la base de données des stations de base et sert de relais pour divers signaux d'alarme destinés au centre d'exploitation et de maintenance. La gestion des ressources radio pour la zone
couverte par les différentes stations de base qui y sont connectées est une autre fonction importante. Cela permet au contrôleur de gérer les transferts intercellulaires des utilisateurs dans sa zone de couverture, c'est- à-dire lorsque une station mobile passe d'une cellule à une autre.[gsm5]

### Network Switching Subsystem (NSS):

The NSS main role is to manage the communications between GSM and other network users. Another task of it includes the main switching functions of GSM, databases required for the subscribers, and mobility management.

### Mobile Station Controller (MSC):

L'interface A relie le centre de commutation mobile au sous-système radio. Son rôle principal est d'assurer la commutation entre les abonnés du réseau mobile et ceux du réseau commuté public (RTC), ou son équivalent numérique, le réseau RNIS (ISDN en anglais). Il fournit divers services aux abonnés, comme la téléphonie, les services supplémentaires et les services de messagerie. Il est également possible de mettre à jour les diverses bases de données (HLR et VLR) qui contiennent toutes les données concernant les abonnés et leur localisation dans le réseau. Les commutateurs MSC d'un opérateur sont connectés l'un à l'autre pour la commutation interne des informations. De manière à garantir une interopérabilité entre les réseaux d'opérateurs, des MSC servant de passerelle (Gateway Mobile Switching Center, GMSC) sont placées en périphérie du réseau d'un opérateur.[gsm5]

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

### Les Interfaces :

 L'interface Um C9est l'interface entre les deux sous systèmes MS et la BTS. On la nomme couramment "interface radio" ou "interface air". • L9interface Abis C9est l9interface entre les deux composants du sous système BSS : la BTS (Base Station Transceiver) et le BSC (Base Station Controler). • L9interface A C9est l9interface entre les deux sous systèmes BSS (Base Station Sub System) et le NSS (Network SubSystem).[4]

## GPRS (General Packet Radio Service) 2.5G:

 As the requirement for sending data on the air-interface increased, new elements such as SGSN (Serving GPRS) and GGSN (Gateway GPRS) were added to the existing GSM system. These elements made it possible to send packet data on the air-interface. This part of the network handling the packet data is also called the 'packet core network'. In addition to the SGSN and GGSN, it also contains the IP routers, firewall servers and DNS (domain name servers). This enables wireless access to the Internet and the bit rate reaching to 150 kbps in optimum conditions.[book12]

## EDGE (Enhanced Data Rates for GSM Evolution) 2.75G:

 The EDGE standard is a mobile telephony standard, an evolution of GSM. This technology adopts a new modulation allowing for higher data rates while using the existing GSM radio spectrum of the operators. Although with limited speeds compared to the UMTS (Universal Mobile Telecommunications System) technologies that follow, EDGE has the capability to offer almost all 3G services. it therefore constitutes an interesting solution for an operator who wishes to offer 3G services using the already existing spectral resources of 2G.[book12]

# The third  generation (3G):

In EDGE, high-volume movement of data was possible, but still the packet transfer on
the air-interface behaves like a circuit switch call. Thus part of this packet connection
efficiency is lost in the circuit switch environment. Moreover, the standards for developing
the networks were different for different parts of the world. Hence, it was decided to have a
network that provides services independent of the technology platform and whose network
design standards are same globally.[book 12]

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









[3] M.A. Rakotomalala, « Evolution des réseaux mobiles », Cours M2-STI-TCO-ESPA, Année Universitaire 2016-2017.

[2]:BOUGUEN, Yannick, HARDOUIN, Eric, et WOLFF, François-Xavier. LTE pour les
reseaux 4G. Editions Eyrolles, 2012. 

6] Jean-Marie Dilhac « Une introduction aux télécommunications », Presses Universitaires du Mirail, 04/10/2012.
[7] JOACHIM Tisal, “Le réseau GSM: l’évolution GPRS, une étape vers l’UMTS”, edition 3,
1999 

[17]POUR, DEVELOPPEMENT D’UNE APPLICATION MOBILE.
"MEMOIRE DE FIN D’ETUDES en vue de l’obtention du DIPLOME de
Master."
