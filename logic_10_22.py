from tkinter import *
import tkinter
from tkinter import filedialog
import csv
import math


# Open Ride Data File & User GPS Trace
gpsFile = filedialog.askopenfilename(initialdir="/", title="Select Ride Data file")
userFile = filedialog.askopenfilename(initialdir="/", title="Select User GPS Trace file")
gpsTrack = open(gpsFile, "r")
userTrack = open(userFile, "r")
csvReader = csv.reader(gpsTrack)
csvReader1 = csv.reader(userTrack)

next(csvReader)
next(csvReader)
next(csvReader)
next(csvReader)
next(csvReader)
header = next(csvReader)
print(header)


header1 = next(csvReader1)
print(header1)


PacketCounterIndex = header.index("PacketCounter")
SampleTimeFineIndex = header.index("SampleTimeFine")
YearIndex = header.index("Year")
MonthIndex = header.index("Month")
DayIndex = header.index("Day")
SecondIndex = header.index("Second")
UTC_NanoIndex = header.index("UTC_Nano")
UTC_YearIndex = header.index("UTC_Year")
UTC_MonthIndex = header.index("UTC_Month")
UTC_DayIndex = header.index("UTC_Day")
UTC_HourIndex = header.index("UTC_Hour")
UTC_MinuteIndex = header.index("UTC_Minute")
UTC_SecondIndex = header.index("UTC_Second")
UTC_ValidIndex = header.index("UTC_Valid")
Acc_XIndex = header.index("Acc_X")
Acc_YIndex = header.index("Acc_Y")
Acc_ZIndex = header.index("Acc_Z")
Gyr_XIndex = header.index("Gyr_X")
Gyr_YIndex = header.index("Gyr_Y")
Gyr_ZIndex = header.index("Gyr_Z")
Mag_XIndex = header.index("Mag_X")
Mag_YIndex = header.index("Mag_Y")
Mag_ZIndex = header.index("Mag_Z")
VelInc_XIndex = header.index("VelInc_X")
VelInc_YIndex = header.index("VelInc_Y")
VelInc_ZIndex = header.index("VelInc_Z")
RollIndex = header.index("Roll")
PitchIndex = header.index("Pitch")
YawIndex = header.index("Yaw")
LatitudeIndex = header.index("Latitude")
LongitudeIndex = header.index("Longitude")
AltitudeIndex = header.index("Altitude")
Vel_XIndex = header.index("Vel_X")
Vel_YIndex = header.index("Vel_Y")
Vel_ZIndex = header.index("Vel_Z")
TemperatureIndex = header.index("Temperature")

UserLatitudeIndex = header1.index("LAT")
UserLongitudeIndex = header1.index("LONG")



# Make an empty list for each data category
PacketCounterList = []
SampleTimeFineList = []
YearList = []
MonthList = []
DayList = []
SecondList = []
UTC_NanoList = []
UTC_YearList = []
UTC_MonthList = []
UTC_DayList = []
UTC_HourList = []
UTC_MinuteList = []
UTC_SecondList = []
UTC_ValidList = []
Acc_XList = []
Acc_YList = []
Acc_ZList = []
Gyr_XList = []
Gyr_YList = []
Gyr_ZList = []
Mag_XList = []
Mag_YList = []
Mag_ZList = []
VelInc_XList = []
VelInc_YList = []
VelInc_ZList = []
RollList = []
PitchList = []
YawList = []
LatitudeList = []
LongitudeList = []
AltitudeList = []
Vel_XList = []
Vel_YList = []
Vel_ZList = []
TemperatureList = []

UserLatitudeList = []
UserLongitudeList = []



for row in csvReader:
    PacketCounter = row[PacketCounterIndex]
    SampleTimeFine= row[SampleTimeFineIndex]
    Year = row[YearIndex]
    Month = row[MonthIndex]
    Day = row[DayIndex]
    Second = row[SecondIndex]
    UTC_Nano = row[UTC_NanoIndex]
    UTC_Year = row[UTC_YearIndex]
    UTC_Month = row[UTC_MonthIndex]
    UTC_Day = row[UTC_DayIndex]
    UTC_Hour = row[UTC_HourIndex]
    UTC_Minute = row[UTC_MinuteIndex]
    UTC_Second = row[UTC_SecondIndex]
    UTC_Valid = row[UTC_ValidIndex]
    Acc_X = row[Acc_XIndex]
    Acc_Y = row[Acc_YIndex]
    Acc_Z = row[Acc_ZIndex]
    Gyr_X = row[Gyr_XIndex]
    Gyr_Y = row[Gyr_YIndex]
    Gyr_Z = row[Gyr_ZIndex]
    Mag_X = row[Mag_XIndex]
    Mag_Y = row[Mag_YIndex]
    Mag_Z = row[Mag_ZIndex]
    VelInc_X = row[Vel_XIndex]
    VelInc_Y = row[Vel_YIndex]
    VelInc_Z = row[Vel_ZIndex]
    Roll = row[RollIndex]
    Pitch = row[PitchIndex]
    Yaw = row[YawIndex]
    Latitude = row[LatitudeIndex]
    Longitude = row[LongitudeIndex]
    Altitude = row[AltitudeIndex]
    Vel_X = row[Vel_XIndex]
    Vel_Y = row[Vel_YIndex]
    Vel_Z = row[Vel_ZIndex]
    Temperature = row[TemperatureIndex]

    # Create Lists for User IMU/GPS Data
    # coordList.append([lat,lon])
    PacketCounterList.extend([PacketCounter])
    SampleTimeFineList.extend([SampleTimeFine])
    YearList.extend([Year])
    MonthList.extend([Month])
    DayList.extend([Day])
    SecondList.extend([Second])
    UTC_NanoList.extend([UTC_Nano])
    UTC_YearList.extend([UTC_Year])
    UTC_MonthList.extend([UTC_Month])
    UTC_DayList.extend([UTC_Day])
    UTC_HourList.extend([UTC_Hour])
    UTC_MinuteList.extend([UTC_Minute])
    UTC_SecondList.extend([UTC_Second])
    UTC_ValidList.extend([UTC_Valid])
    Acc_XList.extend([Acc_X])
    Acc_YList.extend([Acc_Y])
    Acc_ZList.extend([Acc_Z])
    Gyr_XList.extend([Gyr_X])
    Gyr_YList.extend([Gyr_Y])
    Gyr_ZList.extend([Gyr_Z])
    Mag_XList.extend([Mag_X])
    Mag_YList.extend([Mag_Y])
    Mag_ZList.extend([Mag_Z])
    VelInc_XList.extend([VelInc_X])
    VelInc_YList.extend([VelInc_Y])
    VelInc_ZList.extend([VelInc_Z])
    RollList.extend([Roll])
    PitchList.extend([Pitch])
    YawList.extend([Yaw])
    LatitudeList.extend([Latitude])
    LongitudeList.extend([Longitude])
    AltitudeList.extend([Altitude])
    Vel_XList.extend([Vel_X])
    Vel_YList.extend([Vel_Y])
    Vel_ZList.extend([Vel_Z])
    TemperatureList.extend([Temperature])


#Convert Strings of Numbers to Float Values
Acc_XList_Float = [float(i) for i in Acc_XList]
Acc_YList_Float = [float(i) for i in Acc_YList]
Acc_ZList_Float = [float(i) for i in Acc_ZList]









#Create Arrays for User Lat/Long Points
for row in csvReader1:
    UserLongitude = row[UserLongitudeIndex]
    UserLatitude = row[UserLatitudeIndex]

    UserLongitudeList.append([UserLongitude])
    UserLatitudeList.append([UserLatitude])


# Competition Analysis for Acc in X direction
Acc_XThreshold_Positive = 2.5
Acc_XThreshold_Negative = -2.5

Summation = 0.0
Avg = 0.0

for idx, item in enumerate(Acc_XList_Float):
    iterate = idx
    if item > Acc_XThreshold_Positive or item < Acc_XThreshold_Negative:
        for idx2 in range(100):
            if math.isnan(Acc_XList_Float[iterate+idx2]):
                iterate = iterate + 1
            Summation = Summation + Acc_XList_Float[iterate+idx2]
            iterate = iterate + 1
        Avg = Summation/100.0
        if Avg < Acc_XThreshold_Negative:
            print("Violation of Acceleration in X Direction: Hard Brake!")
        elif Avg > Acc_XThreshold_Positive:
            print("Violation of Acceleration in X Direction: Hard Acceleration!")
        else:
            print("No Violation of Acceleration in X Direction has occurred!")
        Summation = 0.0
        Avg = 0.0
    else:
        continue