
Hi from John Vav Vliet
johnkvanvliet2006@yahoo.com

1) unzip the arcive - on Windows I use 7-zip ( http://www.7-zip.org/ )
   For Linux you know what to do for your system 
--------------
2) copy the SatRing.png map to celestia/textures/lores  
--------------
3) edit the solarsys.ssc in celestia/data ( on Windows Notepad will be fine ) it is a normal text file 
4) or place Saturn.ssc in the extras dir.
an example
#########################################################################

"Saturn" "Sol"
{
	Texture "th_saturn.*"
	#Color [ 1.0 1.0 0.85 ]
	HazeColor [ 0.4 0.4 1.4 ]
	HazeDensity 0.25
        #SpecularColor      [ 0.63 0.656 0.595 ] 
        #SpecularPower      0.5
	Radius 60268 # equatorial
	Oblateness 0.0980
        BumpMap "th_saturnbump.*"
	BumpHeight 2.7
	CustomOrbit "vsop87-saturn"
	EllipticalOrbit
	{
	Period           29.4577
	SemiMajorAxis     9.5371
	Eccentricity      0.0542
	Inclination       2.4845
	AscendingNode   113.715
	LongOfPericenter 92.432
        MeanLongitude    49.944
	}

	Atmosphere {
		Height 300
		Lower [ 0.8 0.75 0.65 ]
		Upper [ 0.6 0.55 0.45 ]
		Sky [ 0.8 0.8 0.5 ]
                CloudHeight 100
		CloudSpeed 320
		CloudMap "th_saturnclouds.*"
	}

	RotationPeriod        10.65622 # System III (magnetic field)
	Obliquity             28.049   # 28.052   # old value: 26.73
	EquatorAscendingNode 169.530   # 168.8112 # 169.53
        RotationOffset       358.922   # correct System III prime meridian

	Albedo            0.50

	Rings {                
		Inner   66900                 
		Outer  140225
                Texture "SatRing.png"
	}
}

##########################################################################

then start Celestia and enjoy 
