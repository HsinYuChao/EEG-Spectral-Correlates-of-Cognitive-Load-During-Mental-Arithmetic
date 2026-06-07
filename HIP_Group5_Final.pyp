<?xml version='1.0' encoding='utf-8'?>
<scheme version="2.0" title="HIP_Group_Final" description="">
	<bookmarks>
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
	</bookmarks>
	<nodes>
		<node id="0" name="Parameter Port" qualified_name="widgets.programming.owparameterport.OWParameterPort" project_name="NeuroPype" version="1.3.4" title="Parameter Port&#10;[data (C:/Users/User/Downloads/Subject01_2.edf) (str)]" uuid="0d23c23d-5609-43fb-9f11-9ea3576b9112" position="(25.450000000000003, 202.0375)" />
		<node id="1" name="Stream Data" qualified_name="widgets.formatting.owstreamdata.OWStreamData" project_name="NeuroPype" version="1.3.0" title="Stream Data" uuid="90381f91-e19f-4e1c-8ef0-df67f6d18f75" position="(381.85, 199.99999999999997)" />
		<node id="2" name="Separate Streams" qualified_name="widgets.formatting.owseparatestreams.OWSeparateStreams" project_name="NeuroPype" version="0.5.0" title="Separate Streams&#10;[modality=='EEG']" uuid="ab646e1b-7482-48f0-a250-705d69dc3236" position="(266.97175995492114, 199.99999999999994)" />
		<node id="3" name="Dejitter Timestamps" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" project_name="NeuroPype" version="1.0.0" title="Dejitter Timestamps" uuid="f199189e-d949-4aa6-ac4f-f85ee0b524bf" position="(489.4125000000001, 200.00000000000003)" />
		<node id="4" name="Assign Channel Locations" qualified_name="widgets.source_localization.owassignchannellocations.OWAssignChannelLocations" project_name="NeuroPype" version="1.3.0" title="Assign Channel Locations&#10;[montage: auto]" uuid="6e3689bf-901d-42d1-8f37-27a1d1938fb5" position="(600, 200)" />
		<node id="5" name="Remove Unlocalized Channels" qualified_name="widgets.source_localization.owremoveunlocalizedchannels.OWRemoveUnlocalizedChannels" project_name="NeuroPype" version="1.2.0" title="Remove Unlocalized Channels&#10;[]" uuid="77893434-35b8-499f-8ab7-5c27c409aa12" position="(702.3662668192061, 198.29246636158732)" />
		<node id="6" name="Time Series Plot" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" project_name="NeuroPype" version="1.2.3" title="Time Series Plot&#10;[time x space]" uuid="78d7ef23-8590-4289-b8a3-958444cbec19" position="(837.8124999999998, 68.0625)" />
		<node id="7" name="IIR Filter" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" project_name="NeuroPype" version="1.1.0" title="IIR Filter&#10;[[0.25, 1, 45, 50]Hz bandpass -40dB butter]" uuid="b8ba0caa-28cc-4274-9844-dc9206adf577" position="(819.6625, 201.5125)" />
		<node id="8" name="Detrending" qualified_name="widgets.signal_processing.owdetrend.OWDetrend" project_name="NeuroPype" version="1.0.0" title="Detrending&#10;[linear along time]" uuid="adc33127-f058-4275-a8c1-6b773d2463f0" position="(906.05, 201.51250000000002)" />
		<node id="9" name="Decimate" qualified_name="widgets.signal_processing.owdecimate.OWDecimate" project_name="NeuroPype" version="1.0.1" title="Decimate&#10;[by 2x]" uuid="2e12d9e6-5555-440e-a081-db249f7b9225" position="(1000, 200)" />
		<node id="10" name="Re-referencing" qualified_name="widgets.signal_processing.owrereferencing.OWRereferencing" project_name="NeuroPype" version="1.1.0" title="Re-referencing&#10;[: along space]" uuid="0ebb1aa4-de67-4e9c-aaaa-04aaab63973a" position="(1100, 200)" />
		<node id="11" name="Artifact Removal" qualified_name="widgets.neural.owartifactremoval.OWArtifactRemoval" project_name="NeuroPype" version="2.4.1" title="Artifact Removal&#10;[cutoff:7.5]" uuid="94d70364-ac50-4883-b44e-d72518be91f2" position="(1199.9999999999998, 199.1462331807937)" />
		<node id="12" name="Time Series Plot" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" project_name="NeuroPype" version="1.2.3" title="Time Series Plot&#10;[time x space]" uuid="1e3cb659-a298-49f4-96d6-f2565ca63222" position="(1503.2000000000005, 75.8)" />
		<node id="13" name="Moving Window" qualified_name="widgets.signal_processing.owmovingwindow.OWMovingWindow" project_name="NeuroPype" version="1.1.0" title="Moving Window&#10;[3.0 seconds]" uuid="100db971-07bf-4357-9cb2-fd1ad1f242e4" position="(1300, 200)" />
		<node id="14" name="Power Spectrum (Multitaper)" qualified_name="widgets.spectral.owmultitaperspectrum.OWMultitaperSpectrum" project_name="NeuroPype" version="1.2.1" title="Power Spectrum (Multitaper)&#10;[tbhp:2.5]" uuid="bba74605-967f-4958-99d6-2ece7d338fcc" position="(1400, 200)" />
		<node id="15" name="To Decibels" qualified_name="widgets.elementwise_math.owtodecibels.OWToDecibels" project_name="NeuroPype" version="1.2.2" title="To Decibels&#10;[input is auto-detect]" uuid="02ec9674-015c-438f-9646-23b7a427e2da" position="(1492.4375, -58.637499999999974)" />
		<node id="16" name="Averages" qualified_name="widgets.statistics.owaverages.OWAverages" project_name="NeuroPype" version="1.2.1" title="Averages&#10;[[[1, 4], [4, 8], [8, 12], [12, 30], [30, 50]] Hz along frequency]" uuid="ef8848d5-22c9-40de-9abe-9bf09d6b513f" position="(33.45873318079384, 470.62500000000017)" />
		<node id="17" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.6.0" title="Select Range&#10;[['Fz'] along space (names)]" uuid="71d1924a-f1fe-4de3-97d2-f1c2783c4e76" position="(276.16250000000014, 494.1750000000001)" />
		<node id="18" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.6.0" title="Select Range&#10;[['Pz'] along space (names)]" uuid="f598b434-a0c7-4586-9f03-3d426cc72df8" position="(277.74863226555584, 659.8195068642856)" />
		<node id="19" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.6.0" title="Select Range&#10;[1 along frequency (indices)]" uuid="cf55c559-1971-47b9-826b-72b3a130ed1b" position="(376.16250000000014, 494.1750000000001)" />
		<node id="20" name="Select Range" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" project_name="NeuroPype" version="1.6.0" title="Select Range&#10;[2 along frequency (indices)]" uuid="b6d5e9a1-2b6c-4fc3-9f75-eb08c07b8e82" position="(377.74863226555584, 659.8195068642856)" />
		<node id="21" name="Divide" qualified_name="widgets.elementwise_math.owdivide.OWDivide" project_name="NeuroPype" version="1.1.0" title="Divide&#10;[]" uuid="ce978cf0-0503-4c29-9d69-b63e0ed59647" position="(567.0875000000001, 584.9049663615874)" />
		<node id="22" name="Record to CSV" qualified_name="widgets.file_system.owrecordtocsv.OWRecordToCSV" project_name="NeuroPype" version="1.0.1" title="Record to CSV" uuid="8bb4ebb2-41bb-4d6a-b6bf-2b39c17c7341" position="(1402.3625000000009, 506.41746636158774)" />
		<node id="23" name="Concatenate Data" qualified_name="widgets.tensor_math.owconcatinputs.OWConcatInputs" project_name="NeuroPype" version="1.5.1" title="Concatenate Data&#10;[along feature axis]" uuid="e532f59e-405d-400c-b828-81dbef783ba0" position="(1133.2125, 593.125)" />
		<node id="24" name="Override Axis" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" project_name="NeuroPype" version="1.5.1" title="Override Axis&#10;[space-&gt;feature (only signals)]" uuid="514b3d42-2d44-4dc4-8adc-371fe38559dc" position="(990.4500000000002, 590.8875000000003)" />
		<node id="25" name="Get Directory of Path" qualified_name="widgets.file_system.owpathdirectory.OWPathDirectory" project_name="NeuroPype" version="1.1.0" title="Get Directory of Path" uuid="15a5400b-ae0a-47b9-9f6e-50e2008de930" position="(1124.5875, 390.1500000000001)" />
		<node id="26" name="Get Filename of Path" qualified_name="widgets.file_system.owpathfilename.OWPathFilename" project_name="NeuroPype" version="1.0.0" title="Get Filename of Path" uuid="e1a7dfc3-dc53-463c-af0b-c37618e41c67" position="(983.0125000000002, 391.13750000000005)" />
		<node id="27" name="Parameter Port" qualified_name="widgets.programming.owparameterport.OWParameterPort" project_name="NeuroPype" version="1.3.4" title="Parameter Port&#10;[data (_processed.csv) (str)]" uuid="0c3aecdb-87fb-415b-bd5f-0c641ce721c8" position="(985.8375, 478.1875)" />
		<node id="28" name="Concatenate (String)" qualified_name="widgets.programming.owstringconcat.OWStringConcat" project_name="NeuroPype" version="1.2.0" title="Concatenate (String)&#10;[sep:&quot;&quot;]" uuid="6c2a7f21-56b2-45fa-8b93-91d95be49e5c" position="(1123.9375000000005, 489.82500000000005)" />
		<node id="29" name="Import EDF" qualified_name="widgets.file_system.owimportedf.OWImportEDF" project_name="NeuroPype" version="2.1.0" title="Import EDF&#10;[]" uuid="24305725-3f4c-4f06-8862-c54bd56fff33" position="(146.52363226555562, 197.68834096031688)" />
		<node id="30" name="Spectrum Plot" qualified_name="widgets.visualization.owspectrumplot.OWSpectrumPlot" project_name="NeuroPype" version="2.1.0" title="Spectrum Plot&#10;[PSD x:[0, 50] y:[0, 60] stacked]" uuid="995913ae-00cc-4791-bb20-ce1f872bda33" position="(1586.9057569496617, -58.91782494365143)" />
		<node id="31" name="Power Spectrum (Multitaper)" qualified_name="widgets.spectral.owmultitaperspectrum.OWMultitaperSpectrum" project_name="NeuroPype" version="1.2.1" title="Power Spectrum (Multitaper)&#10;[tbhp:2.5]" uuid="d10402d1-2af4-4aa4-87a5-f7f508aff354" position="(932.9954357625846, -63.07679376408717)" />
		<node id="32" name="Moving Window" qualified_name="widgets.signal_processing.owmovingwindow.OWMovingWindow" project_name="NeuroPype" version="1.1.0" title="Moving Window&#10;[3.0 seconds]" uuid="f51fd4b7-0675-4748-8560-24ce55269f78" position="(832.9954357625846, -63.07679376408717)" />
		<node id="33" name="To Decibels" qualified_name="widgets.elementwise_math.owtodecibels.OWToDecibels" project_name="NeuroPype" version="1.2.2" title="To Decibels&#10;[input is auto-detect]" uuid="b2ea620b-c0ea-420f-b92e-00c35d6578d9" position="(1032.9954357625843, -63.07679376408717)" />
		<node id="34" name="Spectrum Plot" qualified_name="widgets.visualization.owspectrumplot.OWSpectrumPlot" project_name="NeuroPype" version="2.1.0" title="Spectrum Plot&#10;[PSD x:[0, 50] y:[0, 60] stacked]" uuid="141b25bb-7df9-4b55-8935-889467b124b5" position="(1133.5136927122453, -63.35711870773852)" />
	</nodes>
	<links>
		<link id="0" source_node_id="2" sink_node_id="1" source_channel="Matching" sink_channel="Data" enabled="true" />
		<link id="1" source_node_id="1" sink_node_id="3" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="2" source_node_id="3" sink_node_id="4" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="3" source_node_id="4" sink_node_id="5" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="4" source_node_id="5" sink_node_id="6" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="5" source_node_id="5" sink_node_id="7" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="6" source_node_id="8" sink_node_id="9" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="7" source_node_id="9" sink_node_id="10" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="8" source_node_id="10" sink_node_id="11" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="9" source_node_id="7" sink_node_id="8" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="10" source_node_id="11" sink_node_id="12" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="11" source_node_id="13" sink_node_id="14" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="12" source_node_id="14" sink_node_id="15" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="13" source_node_id="16" sink_node_id="17" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="14" source_node_id="16" sink_node_id="18" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="15" source_node_id="17" sink_node_id="19" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="16" source_node_id="18" sink_node_id="20" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="17" source_node_id="19" sink_node_id="21" source_channel="Data" sink_channel="Data1" enabled="true" />
		<link id="18" source_node_id="20" sink_node_id="21" source_channel="Data" sink_channel="Data2" enabled="true" />
		<link id="19" source_node_id="11" sink_node_id="13" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="20" source_node_id="23" sink_node_id="22" source_channel="Outdata" sink_channel="Data" enabled="true" />
		<link id="21" source_node_id="24" sink_node_id="23" source_channel="Data" sink_channel="Data1" enabled="true" />
		<link id="22" source_node_id="0" sink_node_id="25" source_channel="Value" sink_channel="Data" enabled="true" />
		<link id="23" source_node_id="25" sink_node_id="22" source_channel="Data" sink_channel="Output Root" enabled="true" />
		<link id="24" source_node_id="0" sink_node_id="26" source_channel="Value" sink_channel="Data" enabled="true" />
		<link id="25" source_node_id="26" sink_node_id="28" source_channel="Data" sink_channel="Data1" enabled="true" />
		<link id="26" source_node_id="27" sink_node_id="28" source_channel="Value" sink_channel="Data2" enabled="true" />
		<link id="27" source_node_id="28" sink_node_id="22" source_channel="Outstring" sink_channel="Filename" enabled="true" />
		<link id="28" source_node_id="0" sink_node_id="29" source_channel="Value" sink_channel="Filename" enabled="true" />
		<link id="29" source_node_id="29" sink_node_id="2" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="30" source_node_id="15" sink_node_id="30" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="31" source_node_id="14" sink_node_id="16" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="32" source_node_id="21" sink_node_id="24" source_channel="Outdata" sink_channel="Data" enabled="true" />
		<link id="33" source_node_id="32" sink_node_id="31" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="34" source_node_id="31" sink_node_id="33" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="35" source_node_id="33" sink_node_id="34" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="36" source_node_id="5" sink_node_id="32" source_channel="Data" sink_channel="Data" enabled="true" />
	</links>
	<annotations>
		<text id="0" rect="(-20.687141417935948, 133.44006727682537, 150.0, 32.0)" font-family="DejaVu Sans Mono" font-size="16">1. Data Ingestion</text>
		<text id="1" rect="(786.5014642100947, 138.560677207841, 150.0, 69.0)" font-family="DejaVu Sans Mono" font-size="16">3. Temporal Filtering</text>
		<text id="2" rect="(245.95452240284158, 427.49287446212696, 150.0, 32.0)" font-family="DejaVu Sans Mono" font-size="16">Fz</text>
		<text id="3" rect="(247.74863226555584, 604.3195068642856, 150.0, 32.0)" font-family="DejaVu Sans Mono" font-size="16">Pz</text>
		<text id="4" rect="(338.96678249436513, 427.7358564988735, 150.0, 32.0)" font-family="DejaVu Sans Mono" font-size="16">1: theta</text>
		<text id="5" rect="(350.24863226555584, 604.3195068642856, 150.0, 32.0)" font-family="DejaVu Sans Mono" font-size="16">2: alpha</text>
		<text id="6" rect="(348.6055281401542, 142.11929427634726, 106.13750000000005, 35.0)" font-family="DejaVu Sans Mono" font-size="16">Not looping</text>
		<text id="7" rect="(533.9125000000003, 119.175, 192.35000000000002, 63.0)" font-family="DejaVu Sans Mono" font-size="16">2. Spatial Configuration &amp; Channel Cleaning</text>
		<text id="8" rect="(1151.0125, 122.19999999999996, 172.6875, 46.0)" font-family="DejaVu Sans Mono" font-size="16">4. Artifact Removal &amp; Spectral Features</text>
		<text id="9" rect="(1170.6749999999997, -72.9125, 150.0, 32.0)" font-family="DejaVu Sans Mono" font-size="16">PSD_before</text>
		<text id="10" rect="(872.7125000000003, 55.64999999999999, 150.0, 32.0)" font-family="DejaVu Sans Mono" font-size="16">Before Filtering</text>
		<text id="11" rect="(1550.3124999999998, 57.162499999999994, 169.6624999999999, 46.0)" font-family="DejaVu Sans Mono" font-size="16">After Filtering, After AR</text>
		<text id="12" rect="(1616.8624999999997, -69.8875, 150.0, 32.0)" font-family="DejaVu Sans Mono" font-size="16">PSD_after</text>
		<text id="13" rect="(-15.124999999999687, 382.35, 174.20000000000005, 63.0)" font-family="DejaVu Sans Mono" font-size="16">5. Feature Extraction &amp; Workload Calculation</text>
		<text id="14" rect="(716.9250000000002, 476.12500000000006, 207.47500000000014, 46.0)" font-family="DejaVu Sans Mono" font-size="16">6. Data Formatting &amp; Exporting</text>
	</annotations>
	<thumbnail />
	<node_properties>
		<properties node_id="0" format="pickle">gASV9gEAAAAAAAB9lCiMCGF1dG9jYXN0lIiMCWNhbmJlbm9uZZSIjAdkZWZhdWx0lIwnQzovVXNl
cnMvVXNlci9Eb3dubG9hZHMvU3ViamVjdDAxXzIuZWRmlIwEZGVzY5SMDSh1c2UgZGVmYXVsdCmU
jAZkb21haW6UaAaMCGVkaXRhYmxllIiMBmV4cGVydJSJjAtpc19maWxlbmFtZZSJjAppc192aXNp
YmxllIiMCG1ldGFkYXRhlH2UjA1wb3J0X2NhdGVnb3J5lGgGjAhwb3J0bmFtZZSMBGRhdGGUjA1y
ZWxhdGlvbnNoaXBzlF2UjARzYWZllImME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0Ni5zaXCU
jA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAA
AAACLAAAAFUAAAPAAAADCAAAAiwAAABzAAADwAAAAwgAAAAAAAAAAAYAAAACLAAAAHMAAAPAAAAD
CJSFlIeUUpSMBnNlbGVjdJSMBG5vbmWUjBNzZW5kX3NpZ25hbF9jaGFuZ2VklIiMDnNldF9icmVh
a3BvaW50lImMCnZhbHVlX3R5cGWUjANzdHKUjAd2ZXJib3NllImMDHZlcmJvc2VfbmFtZZRoBnUu
</properties>
		<properties node_id="1" format="pickle">gASV0AEAAAAAAAB9lCiMCmRhdGFfZHR5cGWUjAdmbG9hdDY0lIwUZGF0YV9yYW5nZV90b19zdHJl
YW2UjAtsZWdhY3ktd2FybpSMEWhpdGNoX3Byb2JhYmlsaXR5lEcAAAAAAAAAAIwOaml0dGVyX3Bl
cmNlbnSUR0AUAAAAAAAAjAxsb2dfcHJvZ3Jlc3OUiYwHbG9vcGluZ5SJjAhtZXRhZGF0YZR9lIwI
cmFuZHNlZWSUTeeGjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwJUHlRdDYuc2lwlIwOX3VucGlja2xl
X3R5cGWUk5SMDFB5UXQ2LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAABBAAAAFFAAAF
2wAAA/gAAAQQAAABYwAABdsAAAP4AAAAAAAAAAAKAAAABBAAAAFjAAAF2wAAA/iUhZSHlFKUjA5z
ZXRfYnJlYWtwb2ludJSJjAdzcGVlZHVwlEc/8AAAAAAAAIwJc3RhcnRfcG9zlEcAAAAAAAAAAIwQ
dGltZXN0YW1wX2ppdHRlcpRHAAAAAAAAAACMBnRpbWluZ5SMCXdhbGxjbG9ja5SMD3VwZGF0ZV9p
bnRlcnZhbJRHP6R64UeuFHt1Lg==
</properties>
		<properties node_id="2" format="pickle">gASV3gAAAAAAAAB9lCiMCWNvbmRpdGlvbpSMD21vZGFsaXR5PT0nRUVHJ5SMCG1ldGFkYXRhlH2U
jBNzYXZlZFdpZGdldEdlb21ldHJ5lIwJUHlRdDYuc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5
UXQ2LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAABEIAAAIrAAAFqQAAAxMAAARCAAAC
SQAABakAAAMTAAAAAAAAAAAKAAAABEIAAAJJAAAFqQAAAxOUhZSHlFKUjA5zZXRfYnJlYWtwb2lu
dJSJdS4=
</properties>
		<properties node_id="3" format="pickle">gASVGAEAAAAAAAB9lCiMD2ZvcmNlX21vbm90b25pY5SIjA9mb3JnZXRfaGFsZnRpbWWUR0BWgAAA
AAAAjA5tYXhfdXBkYXRlcmF0ZZRN9AGMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdlb21ldHJ5
lIwJUHlRdDYuc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0Q29yZZSMClFCeXRlQXJy
YXmUQ0IB2dDLAAMAAAAAAj0AAADPAAADrwAAAi4AAAI9AAAA7QAAA68AAAIuAAAAAAAAAAAGAAAA
Aj0AAADtAAADrwAAAi6UhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjA53YXJtdXBfc2FtcGxlc5RK
/////3Uu
</properties>
		<properties node_id="4" format="literal">{'force_override': True, 'metadata': {}, 'montage': '(use default)', 'montage_type': 'auto', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'verbose': True}</properties>
		<properties node_id="5" format="pickle">gASV1QAAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjBBwcm90ZWN0X2NoYW5uZWxzlF2UjBNzYXZlZFdp
ZGdldEdlb21ldHJ5lIwJUHlRdDYuc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0Q29y
ZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAjUAAAENAAADtwAAAfEAAAI1AAABKwAAA7cAAAHx
AAAAAAAAAAAGAAAAAjUAAAErAAADtwAAAfGUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJdS4=
</properties>
		<properties node_id="6" format="pickle">gASVnQMAAAAAAAB9lCiMDWFic29sdXRlX3RpbWWUiYwNYWx3YXlzX29uX3RvcJSIjBRhbm5vdGF0
aW9uX2ZvbnRfc2l6ZZRHQCYAAAAAAACMC2FudGlhbGlhc2VklIiMEGF1dG9fbGluZV9jb2xvcnOU
iIwJYXV0b3NjYWxllIiMEGJhY2tncm91bmRfY29sb3KUjAcjMzAzMDMwlIwIY29sb3JtYXCUjAxn
aXN0X3JhaW5ib3eUjBBkZWNvcmF0aW9uX2NvbG9ylIwHI0IwQjBCMJSMCWZvbnRfc2l6ZZRHQCYA
AAAAAACMDGluaXRpYWxfZGltc5RdlChLMksyTfQBTZABZYwObGFiZWxfcm90YXRpb26UjApob3Jp
em9udGFslIwLbGVmdF9vZmZzZXSUSwCMCmxpbmVfY29sb3KUjAV3aGl0ZZSMCmxpbmVfd2lkdGiU
Rz/0AAAAAAAAjAxtYXJrZXJfY29sb3KUjApkYXJrb3JhbmdllIwMbWF4X2NoYW5uZWxzlEsgjAht
ZXRhZGF0YZR9lIwMbmFuc19hc196ZXJvlImMDm5vX2NvbmNhdGVuYXRllImMDm92ZXJyaWRlX3Ny
YXRllIwNKHVzZSBkZWZhdWx0KZSMDHBsb3RfbWFya2Vyc5SJjAtwbG90X21pbm1heJSJjBNzYXZl
ZFdpZGdldEdlb21ldHJ5lIwJUHlRdDYuc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0
Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAABEIAAAFFAAAFqQAAA/gAAARCAAABYwAABakA
AAP4AAAAAAAAAAAKAAAABEIAAAFjAAAFqQAAA/iUhZSHlFKUjAVzY2FsZZRHP/AAAAAAAACMDnNl
dF9icmVha3BvaW50lImMDHNob3dfdG9vbGJhcpSJjAZzdHJlYW2UaB6MC3N0cmVhbV9uYW1llGge
jAx0aWdodF9sYXlvdXSUiIwKdGltZV9yYW5nZZRHQBQAAAAAAACMBXRpdGxllIwQQmVmb3JlIEZp
bHRlcmluZ5SMFXRyYWNrX3dpbmRvd19wb3NpdGlvbpSJjAd2ZXJib3NllImMBnhfYXhpc5SMBHRp
bWWUjAd4X2xhYmVslGgejAZ5X2F4aXOUjAVzcGFjZZSMB3lfbGFiZWyUaB6MCnplcm9fY29sb3KU
jAcjNjA2MDYwlIwIemVyb21lYW6UiHUu
</properties>
		<properties node_id="7" format="pickle">gASVawEAAAAAAAB9lCiMBGF4aXOUjAR0aW1llIwGZGVzaWdulIwGYnV0dGVylIwLZnJlcXVlbmNp
ZXOUXZQoRz/QAAAAAAAASwFLLUsyZYwLaWdub3JlX25hbnOUiYwIbWV0YWRhdGGUfZSMBG1vZGWU
jAhiYW5kcGFzc5SMEG9mZmxpbmVfZmlsdGZpbHSUiYwFb3JkZXKUSwCMCXBhc3NfbG9zc5RHQAgA
AAAAAACME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZST
lIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAAEQQAAAWkAAAWrAAAD1QAA
BEEAAAGHAAAFqwAAA9UAAAAAAAAAAAoAAAAEQQAAAYcAAAWrAAAD1ZSFlIeUUpSMDnNldF9icmVh
a3BvaW50lImMCnN0b3BfYXR0ZW6UR0BEAAAAAAAAdS4=
</properties>
		<properties node_id="8" format="pickle">gASV4AAAAAAAAAB9lCiMBGF4aXOUjAR0aW1llIwIbWV0YWRhdGGUfZSMBm1ldGhvZJSMBmxpbmVh
cpSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwM
UHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAACQgAAAOcAAAOpAAACFgAAAkIA
AAEFAAADqQAAAhYAAAAAAAAAAAYAAAACQgAAAQUAAAOpAAACFpSFlIeUUpSMDnNldF9icmVha3Bv
aW50lIl1Lg==
</properties>
		<properties node_id="9" format="pickle">gASV2QAAAAAAAAB9lCiMBGF4aXOUjAR0aW1llIwGZmFjdG9ylEsCjAhtZXRhZGF0YZR9lIwTc2F2
ZWRXaWRnZXRHZW9tZXRyeZSMCVB5UXQ2LnNpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0Ni5R
dENvcmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAAJCAAAA6QAAA6kAAAIUAAACQgAAAQcAAAOp
AAACFAAAAAAAAAAABgAAAAJCAAABBwAAA6kAAAIUlIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiXUu
</properties>
		<properties node_id="10" format="pickle">gASVWQEAAAAAAAB9lCiMBGF4aXOUjAVzcGFjZZSMCGN1dF9wcm9wlEc/uZmZmZmZmowJZXN0aW1h
dG9ylIwEbWVhbpSMC2lnbm9yZV9uYW5zlImMCG1ldGFkYXRhlH2UjA9yZWZlcmVuY2VfcmFuZ2WU
jAE6lIwOcmVmZXJlbmNlX3VuaXSUjAVuYW1lc5SME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0
Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ
0MsAAwAAAAACGgAAAJEAAAPRAAACbAAAAhoAAACvAAAD0QAAAmwAAAAAAAAAAAYAAAACGgAAAK8A
AAPRAAACbJSFlIeUUpSMDnNldF9icmVha3BvaW50lImMFnVzZV9zZXBhcmF0ZV9yZWZlcmVuY2WU
iYwHdmVyYm9zZZSIdS4=
</properties>
		<properties node_id="11" format="pickle">gASV0gIAAAAAAAB9lCiMAWGUjA0odXNlIGRlZmF1bHQplIwBYpRoAowKYmxvY2tfc2l6ZZRLCowN
Y2FsaWJfc2Vjb25kc5RLHowGY3V0b2ZmlEdAHgAAAAAAAIwPZW1pdF9jYWxpYl9kYXRhlIiMB2lu
aXRfb26UXZSMCWxvb2thaGVhZJRoAowQbWF4X2JhZF9jaGFubmVsc5RHP8mZmZmZmZqMCG1heF9k
aW1zlEcAAAAAAAAAAIwUbWF4X2Ryb3BvdXRfZnJhY3Rpb26URz+5mZmZmZmajAdtYXhfbWVtlE0A
AYwIbWV0YWRhdGGUfZSMEm1pbl9jbGVhbl9mcmFjdGlvbpRHP9AAAAAAAACMFW1pbl9yZXF1aXJl
ZF9jaGFubmVsc5RLAowNcHJlc2VydmVfYmFuZJRoAowKcmllbWFubmlhbpSJjBNzYXZlZFdpZGdl
dEdlb21ldHJ5lIwJUHlRdDYuc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0Q29yZZSM
ClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAABB8AAAFFAAAFzQAAA/gAAAQfAAABYwAABc0AAAP4AAAA
AAAAAAAKAAAABB8AAAFjAAAFzQAAA/iUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjA1zdGRkZXZf
Y3V0b2ZmlEsUjAlzdGVwX3NpemWURz/JmZmZmZmajBB1c2VfY2xlYW5fd2luZG93lIiMCnVzZV9s
ZWdhY3mUiYwWd2luZG93X2xlbl9jbGVhbndpbmRvd5RHP+AAAAAAAACMDXdpbmRvd19sZW5ndGiU
Rz/gAAAAAAAAjA53aW5kb3dfb3ZlcmxhcJRHP+UeuFHrhR+MGndpbmRvd19vdmVybGFwX2NsZWFu
d2luZG93lEc/5R64UeuFH4wRenNjb3JlX3RocmVzaG9sZHOUXZQoSvv///9LB2V1Lg==
</properties>
		<properties node_id="12" format="pickle">gASVpwMAAAAAAAB9lCiMDWFic29sdXRlX3RpbWWUiYwNYWx3YXlzX29uX3RvcJSIjBRhbm5vdGF0
aW9uX2ZvbnRfc2l6ZZRHQCYAAAAAAACMC2FudGlhbGlhc2VklIiMEGF1dG9fbGluZV9jb2xvcnOU
iIwJYXV0b3NjYWxllIiMEGJhY2tncm91bmRfY29sb3KUjAcjMzAzMDMwlIwIY29sb3JtYXCUjAxn
aXN0X3JhaW5ib3eUjBBkZWNvcmF0aW9uX2NvbG9ylIwHI0IwQjBCMJSMCWZvbnRfc2l6ZZRHQCYA
AAAAAACMDGluaXRpYWxfZGltc5RdlChNGgRLMk30AU2QAWWMDmxhYmVsX3JvdGF0aW9ulIwKaG9y
aXpvbnRhbJSMC2xlZnRfb2Zmc2V0lEsAjApsaW5lX2NvbG9ylIwFd2hpdGWUjApsaW5lX3dpZHRo
lEc/9AAAAAAAAIwMbWFya2VyX2NvbG9ylIwKZGFya29yYW5nZZSMDG1heF9jaGFubmVsc5RLIIwI
bWV0YWRhdGGUfZSMDG5hbnNfYXNfemVyb5SJjA5ub19jb25jYXRlbmF0ZZSJjA5vdmVycmlkZV9z
cmF0ZZSMDSh1c2UgZGVmYXVsdCmUjAxwbG90X21hcmtlcnOUiYwLcGxvdF9taW5tYXiUiYwTc2F2
ZWRXaWRnZXRHZW9tZXRyeZSMCVB5UXQ2LnNpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0Ni5R
dENvcmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAAJCAAAAJQAAA6kAAALYAAACQgAAAEMAAAOp
AAAC2AAAAAAAAAAABgAAAAJCAAAAQwAAA6kAAALYlIWUh5RSlIwFc2NhbGWURz/wAAAAAAAAjA5z
ZXRfYnJlYWtwb2ludJSJjAxzaG93X3Rvb2xiYXKUiYwGc3RyZWFtlGgejAtzdHJlYW1fbmFtZZRo
HowMdGlnaHRfbGF5b3V0lIiMCnRpbWVfcmFuZ2WUR0AUAAAAAAAAjAV0aXRsZZSMGUFmdGVyIEZp
bHRlcmluZywgQWZ0ZXIgQVKUjBV0cmFja193aW5kb3dfcG9zaXRpb26UiYwHdmVyYm9zZZSJjAZ4
X2F4aXOUjAR0aW1llIwHeF9sYWJlbJRoHowGeV9heGlzlIwFc3BhY2WUjAd5X2xhYmVslGgejAp6
ZXJvX2NvbG9ylIwHIzYwNjA2MJSMCHplcm9tZWFulIh1Lg==
</properties>
		<properties node_id="13" format="pickle">gASVCAEAAAAAAAB9lCiMD2ZsYWdfYXNfb2ZmbGluZZSJjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRn
ZXRHZW9tZXRyeZSMCVB5UXQ2LnNpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0Ni5RdENvcmWU
jApRQnl0ZUFycmF5lENCAdnQywADAAAAAAIuAAAAywAAA70AAAIyAAACLgAAAOkAAAO9AAACMgAA
AAAAAAAABgAAAAIuAAAA6QAAA70AAAIylIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwEdW5pdJSM
B3NlY29uZHOUjAd2ZXJib3NllImMDXdpbmRvd19sZW5ndGiUR0AIAAAAAAAAdS4=
</properties>
		<properties node_id="14" format="pickle">gASVKAEAAAAAAAB9lCiMGGF2ZXJhZ2Vfb3Zlcl90aW1lX3dpbmRvd5SJjA5oYWxmX2JhbmR3aWR0
aJRHQAQAAAAAAACMCG1ldGFkYXRhlH2UjARuZmZ0lIwNKHVzZSBkZWZhdWx0KZSMCm51bV90YXBl
cnOUaAaMCG9uZXNpZGVklIiME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0Ni5zaXCUjA5fdW5w
aWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAACQAAA
AKwAAAOrAAACUgAAAkAAAADKAAADqwAAAlIAAAAAAAAAAAYAAAACQAAAAMoAAAOrAAACUpSFlIeU
UpSMDnNldF9icmVha3BvaW50lIl1Lg==
</properties>
		<properties node_id="15" format="pickle">gASV9AAAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjA1yZXBsYWNlX3plcm9zlIiME3NhdmVkV2lkZ2V0
R2VvbWV0cnmUjAlQeVF0Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRDb3JllIwK
UUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAACQgAAAQgAAAOpAAACVQAAAkIAAAEmAAADqQAAAlUAAAAA
AAAAAAYAAAACQgAAASYAAAOpAAACVZSFlIeUUpSMDnNldF9icmVha3BvaW50lImMDnNvdXJjZV9t
ZWFzdXJllIwEYXV0b5SMB3ZlcmJvc2WUiHUu
</properties>
		<properties node_id="16" format="pickle">gASVSgEAAAAAAAB9lCiMD2Fubm90YXRlX3Jhbmdlc5SIjARheGlzlIwJZnJlcXVlbmN5lIwLaWdu
b3JlX25hbnOUiYwIbWV0YWRhdGGUfZSMCW9wZXJhdGlvbpSMBG1lYW6UjBNzYXZlZFdpZGdldEdl
b21ldHJ5lIwJUHlRdDYuc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0Q29yZZSMClFC
eXRlQXJyYXmUQ0IB2dDLAAMAAAAAAjsAAACgAAADsQAAAr4AAAI7AAAAvgAAA7EAAAK+AAAAAAAA
AAAGAAAAAjsAAAC+AAADsQAAAr6UhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAR1bml0lIwCSHqU
jAd3aW5kb3dzlF2UKF2UKEsBSwRlXZQoSwRLCGVdlChLCEsMZV2UKEsMSx5lXZQoSx5LMmVldS4=
</properties>
		<properties node_id="17" format="pickle">gASVXAEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwFc3BhY2WUjBBkcm9wX2lmX25vbnJhbmdllIwGbGVnYWN5
lIwQaW52ZXJ0X3NlbGVjdGlvbpSJjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSM
CVB5UXQ2LnNpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0Ni5RdENvcmWUjApRQnl0ZUFycmF5
lENCAdnQywADAAAAAAQoAAABqgAABcMAAAOUAAAEKAAAAcgAAAXDAAADlAAAAAAAAAAACgAAAAQo
AAAByAAABcMAAAOUlIWUh5RSlIwJc2VsZWN0aW9ulF2UjAJGepRhjA5zZXRfYnJlYWtwb2ludJSJ
jAR1bml0lIwFbmFtZXOUdS4=
</properties>
		<properties node_id="18" format="pickle">gASVXAEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwFc3BhY2WUjBBkcm9wX2lmX25vbnJhbmdllIwGbGVnYWN5
lIwQaW52ZXJ0X3NlbGVjdGlvbpSJjAhtZXRhZGF0YZR9lIwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSM
CVB5UXQ2LnNpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0Ni5RdENvcmWUjApRQnl0ZUFycmF5
lENCAdnQywADAAAAAAQoAAABqgAABcMAAAOUAAAEKAAAAcgAAAXDAAADlAAAAAAAAAAACgAAAAQo
AAAByAAABcMAAAOUlIWUh5RSlIwJc2VsZWN0aW9ulF2UjAJQepRhjA5zZXRfYnJlYWtwb2ludJSJ
jAR1bml0lIwFbmFtZXOUdS4=
</properties>
		<properties node_id="19" format="pickle">gASVXAEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwJZnJlcXVlbmN5lIwQZHJvcF9pZl9ub25yYW5nZZSMBmxl
Z2FjeZSMEGludmVydF9zZWxlY3Rpb26UiYwIbWV0YWRhdGGUfZSME3NhdmVkV2lkZ2V0R2VvbWV0
cnmUjAlQeVF0Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVB
cnJheZRDQgHZ0MsAAwAAAAACKAAAAIoAAAPDAAACdAAAAigAAACoAAADwwAAAnQAAAAAAAAAAAYA
AAACKAAAAKgAAAPDAAACdJSFlIeUUpSMCXNlbGVjdGlvbpRLAYwOc2V0X2JyZWFrcG9pbnSUiYwE
dW5pdJSMB2luZGljZXOUdS4=
</properties>
		<properties node_id="20" format="pickle">gASVXAEAAAAAAAB9lCiME2FwcGx5X211bHRpcGxlX2F4ZXOUiYwfYXBwbHlfdGltZV9zZWxlY3Rp
b25fdG9fbWFya2Vyc5SJjARheGlzlIwJZnJlcXVlbmN5lIwQZHJvcF9pZl9ub25yYW5nZZSMBmxl
Z2FjeZSMEGludmVydF9zZWxlY3Rpb26UiYwIbWV0YWRhdGGUfZSME3NhdmVkV2lkZ2V0R2VvbWV0
cnmUjAlQeVF0Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVB
cnJheZRDQgHZ0MsAAwAAAAACKAAAAIoAAAPDAAACdAAAAigAAACoAAADwwAAAnQAAAAAAAAAAAYA
AAACKAAAAKgAAAPDAAACdJSFlIeUUpSMCXNlbGVjdGlvbpRLAowOc2V0X2JyZWFrcG9pbnSUiYwE
dW5pdJSMB2luZGljZXOUdS4=
</properties>
		<properties node_id="21" format="pickle">gASVJgEAAAAAAAB9lCiMDGF4aXNfcGFpcmluZ5SMB2RlZmF1bHSUjAVkYXRhMpSMDSh1c2UgZGVm
YXVsdCmUjA1sYWJlbF9wYWlyaW5nlIwEYXV0b5SMD2xpc3RzX2FzX2FycmF5c5SJjAhtZXRhZGF0
YZR9lIwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSMCVB5UXQ2LnNpcJSMDl91bnBpY2tsZV90eXBllJOU
jAxQeVF0Ni5RdENvcmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAARCAAAB3AAABakAAANhAAAE
QgAAAfoAAAWpAAADYQAAAAAAAAAACgAAAARCAAAB+gAABakAAANhlIWUh5RSlIwOc2V0X2JyZWFr
cG9pbnSUiYwHdmVyYm9zZZSIdS4=
</properties>
		<properties node_id="22" format="pickle">gASVswEAAAAAAAB9lCiMF2Fic29sdXRlX2luc3RhbmNlX3RpbWVzlIiMDWNsb3VkX2FjY291bnSU
jA0odXNlIGRlZmF1bHQplIwMY2xvdWRfYnVja2V0lGgDjBFjbG91ZF9jcmVkZW50aWFsc5RoA4wK
Y2xvdWRfaG9zdJSMB0RlZmF1bHSUjA1jb2x1bW5faGVhZGVylIiMDGRlbGV0ZV9wYXJ0c5SIjAhm
aWxlbmFtZZRoA4wIbWV0YWRhdGGUfZSMC291dHB1dF9yb290lGgDjAtyZXRyaWV2YWJsZZSJjBNz
YXZlZFdpZGdldEdlb21ldHJ5lIwJUHlRdDYuc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2
LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAkIAAABbAAADqQAAAwIAAAJCAAAAeQAA
A6kAAAMCAAAAAAAAAAAGAAAAAkIAAAB5AAADqQAAAwKUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJ
jAt0aW1lX3N0YW1wc5SIjA90aW1lc3RhbXBfbGFiZWyUjAl0aW1lc3RhbXCUdS4=
</properties>
		<properties node_id="23" format="pickle">gASVcwEAAAAAAAB9lCiMDWFsbG93X21hcmtlcnOUjARhdXRvlIwEYXhpc5SMB2ZlYXR1cmWUjAtj
aHVua19wcm9wc5SMBWZpcnN0lIwNY29ycmVjdF9vcmRlcpSIjApjcmVhdGVfbmV3lImMCG1ldGFk
YXRhlH2UjBVuZXdfYXhpc19jdXN0b21fbGFiZWyUjA0odXNlIGRlZmF1bHQplIwKcHJvcGVydGll
c5RoDIwPcmVxdWlyZWRfaW5wdXRzlEsAjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwJUHlRdDYuc2lw
lIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMA
AAAAAkIAAABHAAADqQAAArcAAAJCAAAAZQAAA6kAAAK3AAAAAAAAAAAGAAAAAkIAAABlAAADqQAA
AreUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAd2ZXJib3NllIh1Lg==
</properties>
		<properties node_id="24" format="pickle">gASVxwEAAAAAAAB9lCiMDGF4aXNfY2FjaGluZ5SIjA9heGlzX29jY3VycmVuY2WUSwCMEGNhcnJ5
X292ZXJfbmFtZXOUiIwSY2Fycnlfb3Zlcl9udW1iZXJzlIiMDGN1c3RvbV9sYWJlbJSMDSh1c2Ug
ZGVmYXVsdCmUjAhkZWNpbWFsc5RLA4wJaW5pdF9kYXRhlGgGjAtqb2luX2Zvcm1hdJSMBXtuZXd9
lIwRa2VlcF9vdGhlcl9hcnJheXOUiYwKa2VlcF9wcm9wc5SJjAhtZXRhZGF0YZR9lIwIbmV3X2F4
aXOUjAdmZWF0dXJllIwIb2xkX2F4aXOUjAVzcGFjZZSMDG9ubHlfc2lnbmFsc5SIjBNzYXZlZFdp
ZGdldEdlb21ldHJ5lIwJUHlRdDYuc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0Q29y
ZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAABEIAAAFFAAAFqQAAA/gAAARCAAABYwAABakAAAP4
AAAAAAAAAAAKAAAABEIAAAFjAAAFqQAAA/iUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjAl2ZXJi
b3NpdHmUSwB1Lg==
</properties>
		<properties node_id="25" format="pickle">gASV1QAAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwJUHlRdDYu
c2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDL
AAMAAAAABEIAAAJAAAAFqQAAAv0AAARCAAACXgAABakAAAL9AAAAAAAAAAAKAAAABEIAAAJeAAAF
qQAAAv2UhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjBF0cmltX3BsYWNlaG9sZGVyc5SIdS4=
</properties>
		<properties node_id="26" format="literal">{'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties node_id="27" format="pickle">gASV3QEAAAAAAAB9lCiMCGF1dG9jYXN0lIiMCWNhbmJlbm9uZZSIjAdkZWZhdWx0lIwOX3Byb2Nl
c3NlZC5jc3aUjARkZXNjlIwNKHVzZSBkZWZhdWx0KZSMBmRvbWFpbpRoBowIZWRpdGFibGWUiIwG
ZXhwZXJ0lImMC2lzX2ZpbGVuYW1llImMCmlzX3Zpc2libGWUiIwIbWV0YWRhdGGUfZSMDXBvcnRf
Y2F0ZWdvcnmUaAaMCHBvcnRuYW1llIwEZGF0YZSMDXJlbGF0aW9uc2hpcHOUXZSMBHNhZmWUiYwT
c2F2ZWRXaWRnZXRHZW9tZXRyeZSMCVB5UXQ2LnNpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0
Ni5RdENvcmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAAQsAAABRQAABcAAAAP4AAAELAAAAWMA
AAXAAAAD+AAAAAAAAAAACgAAAAQsAAABYwAABcAAAAP4lIWUh5RSlIwGc2VsZWN0lIwEbm9uZZSM
E3NlbmRfc2lnbmFsX2NoYW5nZWSUiIwOc2V0X2JyZWFrcG9pbnSUiYwKdmFsdWVfdHlwZZSMA3N0
cpSMB3ZlcmJvc2WUiYwMdmVyYm9zZV9uYW1llGgGdS4=
</properties>
		<properties node_id="28" format="pickle">gASV3AAAAAAAAAB9lCiMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwJUHlRdDYu
c2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDL
AAMAAAAABEIAAAItAAAFqQAAAxEAAARCAAACSwAABakAAAMRAAAAAAAAAAAKAAAABEIAAAJLAAAF
qQAAAxGUhZSHlFKUjAlzZXBhcmF0b3KUjA0odXNlIGRlZmF1bHQplIwOc2V0X2JyZWFrcG9pbnSU
iXUu
</properties>
		<properties node_id="29" format="literal">{'cloud_account': '(use default)', 'cloud_bucket': '(use default)', 'cloud_credentials': '(use default)', 'cloud_host': 'Default', 'exclude_channels': [], 'filename': '(use default)', 'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'stim_channel': '(use default)', 'strip_modality': True, 'unit': 'uV'}</properties>
		<properties node_id="30" format="pickle">gASVLwMAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiIwUYW5ub3RhdGlvbl9mb250X3NpemWUR0Am
AAAAAAAAjAthbnRpYWxpYXNlZJSIjBBhdXRvX2xpbmVfY29sb3JzlIiMCWF1dG9zY2FsZZSJjBBi
YWNrZ3JvdW5kX2NvbG9ylIwHIzMwMzAzMJSMCGNvbG9ybWFwlIwMZ2lzdF9yYWluYm93lIwQZGVj
b3JhdGlvbl9jb2xvcpSMByNCMEIwQjCUjAlmb250X3NpemWUR0AmAAAAAAAAjAxpbml0aWFsX2Rp
bXOUXZQoSzJLMk3oA00gA2WMDmxhYmVsX3JvdGF0aW9ulIwKaG9yaXpvbnRhbJSMC2xlZnRfb2Zm
c2V0lEsAjApsaW5lX2NvbG9ylIwFd2hpdGWUjApsaW5lX3dpZHRolEc/9AAAAAAAAIwMbWF4X2No
YW5uZWxzlEsgjAhtZXRhZGF0YZR9lIwVb25lX292ZXJfZl9jb3JyZWN0aW9ulIiMC3Bsb3RfbWlu
bWF4lImME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZST
lIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAACQgAAAD0AAAOpAAAC8AAA
AkIAAABbAAADqQAAAvAAAAAAAAAAAAYAAAACQgAAAFsAAAOpAAAC8JSFlIeUUpSMBXNjYWxllIwN
KHVzZSBkZWZhdWx0KZSMDnNldF9icmVha3BvaW50lImMDHNob3dfdG9vbGJhcpSJjAdzdGFja2Vk
lIiMBnN0cmVhbZRoJYwLc3RyZWFtX25hbWWUaCWMDHRpZ2h0X2xheW91dJSIjAV0aXRsZZSMCVBT
RF9hZnRlcpSMFXRyYWNrX3dpbmRvd19wb3NpdGlvbpSJjAR1bml0lIwDUFNElIwHdmVyYm9zZZSJ
jAd4X2xhYmVslGgljAd4X3JhbmdllF2UKEsASzJljAd5X2xhYmVslGgljAd5X3JhbmdllF2UKEsA
SzxljAp6ZXJvX2NvbG9ylIwHIzYwNjA2MJR1Lg==
</properties>
		<properties node_id="31" format="literal">{'average_over_time_window': False, 'half_bandwidth': 2.5, 'metadata': {}, 'nfft': '(use default)', 'num_tapers': '(use default)', 'onesided': True, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties node_id="32" format="literal">{'flag_as_offline': False, 'metadata': {}, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'unit': 'seconds', 'verbose': False, 'window_length': 3.0}</properties>
		<properties node_id="33" format="literal">{'metadata': {}, 'replace_zeros': True, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'source_measure': 'auto', 'verbose': True}</properties>
		<properties node_id="34" format="pickle">gASVMAMAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiIwUYW5ub3RhdGlvbl9mb250X3NpemWUR0Am
AAAAAAAAjAthbnRpYWxpYXNlZJSIjBBhdXRvX2xpbmVfY29sb3JzlIiMCWF1dG9zY2FsZZSJjBBi
YWNrZ3JvdW5kX2NvbG9ylIwHIzMwMzAzMJSMCGNvbG9ybWFwlIwMZ2lzdF9yYWluYm93lIwQZGVj
b3JhdGlvbl9jb2xvcpSMByNCMEIwQjCUjAlmb250X3NpemWUR0AmAAAAAAAAjAxpbml0aWFsX2Rp
bXOUXZQoSzJLMk3oA00gA2WMDmxhYmVsX3JvdGF0aW9ulIwKaG9yaXpvbnRhbJSMC2xlZnRfb2Zm
c2V0lEsAjApsaW5lX2NvbG9ylIwFd2hpdGWUjApsaW5lX3dpZHRolEc/9AAAAAAAAIwMbWF4X2No
YW5uZWxzlEsTjAhtZXRhZGF0YZR9lIwVb25lX292ZXJfZl9jb3JyZWN0aW9ulIiMC3Bsb3RfbWlu
bWF4lImME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZST
lIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAACQgAAAD0AAAOpAAAC8AAA
AkIAAABbAAADqQAAAvAAAAAAAAAAAAYAAAACQgAAAFsAAAOpAAAC8JSFlIeUUpSMBXNjYWxllIwN
KHVzZSBkZWZhdWx0KZSMDnNldF9icmVha3BvaW50lImMDHNob3dfdG9vbGJhcpSJjAdzdGFja2Vk
lIiMBnN0cmVhbZRoJYwLc3RyZWFtX25hbWWUaCWMDHRpZ2h0X2xheW91dJSIjAV0aXRsZZSMClBT
RF9iZWZvcmWUjBV0cmFja193aW5kb3dfcG9zaXRpb26UiYwEdW5pdJSMA1BTRJSMB3ZlcmJvc2WU
iYwHeF9sYWJlbJRoJYwHeF9yYW5nZZRdlChLAEsyZYwHeV9sYWJlbJRoJYwHeV9yYW5nZZRdlChL
AEs8ZYwKemVyb19jb2xvcpSMByM2MDYwNjCUdS4=
</properties>
	</node_properties>
	<patch>{"description": {"description": "", "license": "", "name": "HIP_Group_Final", "status": "(unspecified)", "url": "", "version": "0.0.0"}, "edges": [["node3", "matching", "node2", "data"], ["node2", "data", "node4", "data"], ["node4", "data", "node5", "data"], ["node5", "data", "node6", "data"], ["node6", "data", "node7", "data"], ["node6", "data", "node8", "data"], ["node6", "data", "node33", "data"], ["node9", "data", "node10", "data"], ["node10", "data", "node11", "data"], ["node11", "data", "node12", "data"], ["node8", "data", "node9", "data"], ["node12", "data", "node13", "data"], ["node12", "data", "node14", "data"], ["node14", "data", "node15", "data"], ["node15", "data", "node16", "data"], ["node15", "data", "node17", "data"], ["node17", "data", "node18", "data"], ["node17", "data", "node19", "data"], ["node18", "data", "node20", "data"], ["node19", "data", "node21", "data"], ["node20", "data", "node22", "data1"], ["node21", "data", "node22", "data2"], ["node25", "data", "node24", "data1"], ["node27", "data", "node29", "data1"], ["node28", "value", "node29", "data2"], ["node1", "value", "node30", "filename"], ["node1", "value", "node26", "data"], ["node1", "value", "node27", "data"], ["node30", "data", "node3", "data"], ["node16", "data", "node31", "data"], ["node22", "outdata", "node25", "data"], ["node33", "data", "node32", "data"], ["node32", "data", "node34", "data"], ["node34", "data", "node35", "data"], ["node24", "outdata", "node23", "data"], ["node29", "outstring", "node23", "filename"], ["node26", "data", "node23", "output_root"]], "nodes": {"node1": {"class": "ParameterPort", "module": "neuropype.nodes.programming.ParameterPort", "params": {"autocast": {"customized": false, "type": "BoolPort", "value": true}, "canbenone": {"customized": false, "type": "BoolPort", "value": true}, "default": {"customized": true, "type": "Port", "value": "C:/Users/User/Downloads/Subject01_2.edf"}, "desc": {"customized": false, "type": "StringPort", "value": ""}, "domain": {"customized": false, "type": "Port", "value": null}, "editable": {"customized": false, "type": "BoolPort", "value": true}, "expert": {"customized": false, "type": "BoolPort", "value": false}, "is_filename": {"customized": false, "type": "BoolPort", "value": false}, "is_visible": {"customized": false, "type": "BoolPort", "value": true}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "port_category": {"customized": false, "type": "StringPort", "value": ""}, "portname": {"customized": false, "type": "StringPort", "value": "data"}, "relationships": {"customized": false, "type": "ListPort", "value": []}, "safe": {"customized": false, "type": "BoolPort", "value": false}, "select": {"customized": false, "type": "EnumPort", "value": "none"}, "send_signal_changed": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "value_type": {"customized": false, "type": "EnumPort", "value": "str"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "verbose_name": {"customized": false, "type": "StringPort", "value": null}}, "uuid": "0d23c23d-5609-43fb-9f11-9ea3576b9112"}, "node10": {"class": "Decimate", "module": "neuropype.nodes.signal_processing.Decimate", "params": {"axis": {"customized": false, "type": "ComboPort", "value": "time"}, "factor": {"customized": false, "type": "IntPort", "value": 2}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "2e12d9e6-5555-440e-a081-db249f7b9225"}, "node11": {"class": "Rereferencing", "module": "neuropype.nodes.signal_processing.Rereferencing", "params": {"axis": {"customized": false, "type": "ComboPort", "value": "space"}, "cut_prop": {"customized": false, "type": "FloatPort", "value": 0.1}, "estimator": {"customized": false, "type": "EnumPort", "value": "mean"}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "reference_range": {"customized": false, "type": "Port", "value": ":"}, "reference_unit": {"customized": true, "type": "EnumPort", "value": "names"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "use_separate_reference": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "0ebb1aa4-de67-4e9c-aaaa-04aaab63973a"}, "node12": {"class": "ArtifactRemoval", "module": "neuropype.nodes.neural.ArtifactRemoval", "params": {"a": {"customized": false, "type": "Port", "value": null}, "b": {"customized": false, "type": "Port", "value": null}, "block_size": {"customized": true, "type": "IntPort", "value": 10}, "calib_seconds": {"customized": true, "type": "IntPort", "value": 30}, "cutoff": {"customized": false, "type": "FloatPort", "value": 7.5}, "emit_calib_data": {"customized": false, "type": "BoolPort", "value": true}, "init_on": {"customized": false, "type": "ListPort", "value": []}, "lookahead": {"customized": false, "type": "Port", "value": null}, "max_bad_channels": {"customized": false, "type": "FloatPort", "value": 0.2}, "max_dims": {"customized": false, "type": "FloatPort", "value": 0.0}, "max_dropout_fraction": {"customized": false, "type": "FloatPort", "value": 0.1}, "max_mem": {"customized": false, "type": "Port", "value": 256}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "min_clean_fraction": {"customized": false, "type": "FloatPort", "value": 0.25}, "min_required_channels": {"customized": false, "type": "IntPort", "value": 2}, "preserve_band": {"customized": false, "type": "DictPort", "value": null}, "riemannian": {"customized": false, "type": "BoolPort", "value": false}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stddev_cutoff": {"customized": false, "type": "IntPort", "value": 20}, "step_size": {"customized": false, "type": "FloatPort", "value": 0.2}, "use_clean_window": {"customized": false, "type": "BoolPort", "value": true}, "use_legacy": {"customized": false, "type": "BoolPort", "value": false}, "window_len_cleanwindow": {"customized": false, "type": "FloatPort", "value": 0.5}, "window_length": {"customized": false, "type": "FloatPort", "value": 0.5}, "window_overlap": {"customized": false, "type": "FloatPort", "value": 0.66}, "window_overlap_cleanwindow": {"customized": false, "type": "FloatPort", "value": 0.66}, "zscore_thresholds": {"customized": false, "type": "ListPort", "value": [-5, 7]}}, "uuid": "94d70364-ac50-4883-b44e-d72518be91f2"}, "node13": {"class": "TimeSeriesPlot", "module": "neuropype.nodes.visualization.TimeSeriesPlot", "params": {"absolute_time": {"customized": false, "type": "BoolPort", "value": false}, "always_on_top": {"customized": true, "type": "BoolPort", "value": true}, "annotation_font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": true}, "autoscale": {"customized": false, "type": "BoolPort", "value": true}, "background_color": {"customized": false, "type": "StringPort", "value": "#303030"}, "colormap": {"customized": false, "type": "EnumPort", "value": "gist_rainbow"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#B0B0B0"}, "font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "initial_dims": {"customized": true, "type": "ListPort", "value": [1050, 50, 500, 400]}, "label_rotation": {"customized": false, "type": "EnumPort", "value": "horizontal"}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "line_color": {"customized": false, "type": "StringPort", "value": "white"}, "line_width": {"customized": false, "type": "FloatPort", "value": 1.25}, "marker_color": {"customized": false, "type": "Port", "value": "darkorange"}, "max_channels": {"customized": false, "type": "IntPort", "value": 32}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nans_as_zero": {"customized": false, "type": "BoolPort", "value": false}, "no_concatenate": {"customized": false, "type": "BoolPort", "value": false}, "override_srate": {"customized": false, "type": "FloatPort", "value": null}, "plot_markers": {"customized": false, "type": "BoolPort", "value": false}, "plot_minmax": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": false, "type": "FloatPort", "value": 1.0}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stream": {"customized": false, "type": "StringPort", "value": null}, "stream_name": {"customized": false, "type": "AliasPort", "value": null}, "tight_layout": {"customized": false, "type": "BoolPort", "value": true}, "time_range": {"customized": false, "type": "FloatPort", "value": 5.0}, "title": {"customized": true, "type": "StringPort", "value": "After Filtering, After AR"}, "track_window_position": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "x_axis": {"customized": false, "type": "ComboPort", "value": "time"}, "x_label": {"customized": false, "type": "StringPort", "value": ""}, "y_axis": {"customized": false, "type": "ComboPort", "value": "space"}, "y_label": {"customized": false, "type": "StringPort", "value": ""}, "zero_color": {"customized": false, "type": "StringPort", "value": "#606060"}, "zeromean": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "1e3cb659-a298-49f4-96d6-f2565ca63222"}, "node14": {"class": "MovingWindow", "module": "neuropype.nodes.signal_processing.MovingWindow", "params": {"flag_as_offline": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": false, "type": "EnumPort", "value": "seconds"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "window_length": {"customized": true, "type": "FloatPort", "value": 3.0}}, "uuid": "100db971-07bf-4357-9cb2-fd1ad1f242e4"}, "node15": {"class": "MultitaperSpectrum", "module": "neuropype.nodes.spectral.MultitaperSpectrum", "params": {"average_over_time_window": {"customized": false, "type": "BoolPort", "value": false}, "half_bandwidth": {"customized": false, "type": "FloatPort", "value": 2.5}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nfft": {"customized": false, "type": "IntPort", "value": null}, "num_tapers": {"customized": false, "type": "IntPort", "value": null}, "onesided": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "bba74605-967f-4958-99d6-2ece7d338fcc"}, "node16": {"class": "ToDecibels", "module": "neuropype.nodes.elementwise_math.ToDecibels", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "replace_zeros": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "source_measure": {"customized": false, "type": "EnumPort", "value": "auto"}, "verbose": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "02ec9674-015c-438f-9646-23b7a427e2da"}, "node17": {"class": "Averages", "module": "neuropype.nodes.statistics.Averages", "params": {"annotate_ranges": {"customized": false, "type": "BoolPort", "value": true}, "axis": {"customized": true, "type": "ComboPort", "value": "frequency"}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "operation": {"customized": false, "type": "EnumPort", "value": "mean"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "Hz"}, "windows": {"customized": true, "type": "ListPort", "value": [[1, 4], [4, 8], [8, 12], [12, 30], [30, 50]]}}, "uuid": "ef8848d5-22c9-40de-9abe-9bf09d6b513f"}, "node18": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "ComboPort", "value": "space"}, "drop_if_nonrange": {"customized": false, "type": "EnumPort", "value": "legacy"}, "invert_selection": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": ["Fz"]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "ComboPort", "value": "names"}}, "uuid": "71d1924a-f1fe-4de3-97d2-f1c2783c4e76"}, "node19": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "ComboPort", "value": "space"}, "drop_if_nonrange": {"customized": false, "type": "EnumPort", "value": "legacy"}, "invert_selection": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": ["Pz"]}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "ComboPort", "value": "names"}}, "uuid": "f598b434-a0c7-4586-9f03-3d426cc72df8"}, "node2": {"class": "StreamData", "module": "neuropype.nodes.formatting.StreamData", "params": {"data_dtype": {"customized": false, "type": "EnumPort", "value": "float64"}, "data_range_to_stream": {"customized": false, "type": "EnumPort", "value": "legacy-warn"}, "hitch_probability": {"customized": false, "type": "FloatPort", "value": 0.0}, "jitter_percent": {"customized": false, "type": "FloatPort", "value": 5.0}, "log_progress": {"customized": false, "type": "BoolPort", "value": false}, "looping": {"customized": true, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "randseed": {"customized": false, "type": "IntPort", "value": 34535}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "speedup": {"customized": false, "type": "FloatPort", "value": 1.0}, "start_pos": {"customized": false, "type": "FloatPort", "value": 0.0}, "timestamp_jitter": {"customized": false, "type": "FloatPort", "value": 0.0}, "timing": {"customized": false, "type": "EnumPort", "value": "wallclock"}, "update_interval": {"customized": false, "type": "FloatPort", "value": 0.04}}, "uuid": "90381f91-e19f-4e1c-8ef0-df67f6d18f75"}, "node20": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "ComboPort", "value": "frequency"}, "drop_if_nonrange": {"customized": false, "type": "EnumPort", "value": "legacy"}, "invert_selection": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": 1}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": false, "type": "ComboPort", "value": "indices"}}, "uuid": "cf55c559-1971-47b9-826b-72b3a130ed1b"}, "node21": {"class": "SelectRange", "module": "neuropype.nodes.tensor_math.SelectRange", "params": {"apply_multiple_axes": {"customized": false, "type": "BoolPort", "value": false}, "apply_time_selection_to_markers": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": true, "type": "ComboPort", "value": "frequency"}, "drop_if_nonrange": {"customized": false, "type": "EnumPort", "value": "legacy"}, "invert_selection": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "selection": {"customized": true, "type": "Port", "value": 2}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": false, "type": "ComboPort", "value": "indices"}}, "uuid": "b6d5e9a1-2b6c-4fc3-9f75-eb08c07b8e82"}, "node22": {"class": "Divide", "module": "neuropype.nodes.elementwise_math.Divide", "params": {"axis_pairing": {"customized": false, "type": "EnumPort", "value": "default"}, "data2": {"customized": false, "type": "Port", "value": null}, "label_pairing": {"customized": false, "type": "EnumPort", "value": "auto"}, "lists_as_arrays": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "ce978cf0-0503-4c29-9d69-b63e0ed59647"}, "node23": {"class": "RecordToCSV", "module": "neuropype.nodes.file_system.RecordToCSV", "params": {"absolute_instance_times": {"customized": false, "type": "BoolPort", "value": true}, "cloud_account": {"customized": false, "type": "StringPort", "value": ""}, "cloud_bucket": {"customized": false, "type": "StringPort", "value": ""}, "cloud_credentials": {"customized": false, "type": "StringPort", "value": ""}, "cloud_host": {"customized": false, "type": "EnumPort", "value": "Default"}, "column_header": {"customized": false, "type": "BoolPort", "value": true}, "delete_parts": {"customized": false, "type": "BoolPort", "value": true}, "filename": {"customized": true, "type": "StringPort", "value": null}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "output_root": {"customized": false, "type": "StringPort", "value": ""}, "retrievable": {"customized": false, "type": "BoolPort", "value": false}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "time_stamps": {"customized": false, "type": "BoolPort", "value": true}, "timestamp_label": {"customized": false, "type": "StringPort", "value": "timestamp"}}, "uuid": "8bb4ebb2-41bb-4d6a-b6bf-2b39c17c7341"}, "node24": {"class": "ConcatInputs", "module": "neuropype.nodes.tensor_math.ConcatInputs", "params": {"allow_markers": {"customized": false, "type": "EnumPort", "value": "auto"}, "axis": {"customized": true, "type": "ComboPort", "value": "feature"}, "chunk_props": {"customized": false, "type": "EnumPort", "value": "first"}, "correct_order": {"customized": false, "type": "BoolPort", "value": true}, "create_new": {"customized": true, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "new_axis_custom_label": {"customized": false, "type": "StringPort", "value": null}, "properties": {"customized": false, "type": "ListPort", "value": null}, "required_inputs": {"customized": false, "type": "IntPort", "value": 0}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "e532f59e-405d-400c-b828-81dbef783ba0"}, "node25": {"class": "OverrideAxis", "module": "neuropype.nodes.tensor_math.OverrideAxis", "params": {"axis_caching": {"customized": false, "type": "BoolPort", "value": true}, "axis_occurrence": {"customized": false, "type": "IntPort", "value": 0}, "carry_over_names": {"customized": false, "type": "BoolPort", "value": true}, "carry_over_numbers": {"customized": false, "type": "BoolPort", "value": true}, "custom_label": {"customized": false, "type": "StringPort", "value": ""}, "decimals": {"customized": false, "type": "IntPort", "value": 3}, "init_data": {"customized": false, "type": "ListPort", "value": null}, "join_format": {"customized": false, "type": "StringPort", "value": "{new}"}, "keep_other_arrays": {"customized": false, "type": "BoolPort", "value": false}, "keep_props": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "new_axis": {"customized": true, "type": "ComboPort", "value": "feature"}, "old_axis": {"customized": true, "type": "ComboPort", "value": "space"}, "only_signals": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "verbosity": {"customized": false, "type": "IntPort", "value": 0}}, "uuid": "514b3d42-2d44-4dc4-8adc-371fe38559dc"}, "node26": {"class": "PathDirectory", "module": "neuropype.nodes.file_system.PathDirectory", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_placeholders": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "15a5400b-ae0a-47b9-9f6e-50e2008de930"}, "node27": {"class": "PathFilename", "module": "neuropype.nodes.file_system.PathFilename", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "e1a7dfc3-dc53-463c-af0b-c37618e41c67"}, "node28": {"class": "ParameterPort", "module": "neuropype.nodes.programming.ParameterPort", "params": {"autocast": {"customized": false, "type": "BoolPort", "value": true}, "canbenone": {"customized": false, "type": "BoolPort", "value": true}, "default": {"customized": true, "type": "Port", "value": "_processed.csv"}, "desc": {"customized": false, "type": "StringPort", "value": ""}, "domain": {"customized": false, "type": "Port", "value": null}, "editable": {"customized": false, "type": "BoolPort", "value": true}, "expert": {"customized": false, "type": "BoolPort", "value": false}, "is_filename": {"customized": false, "type": "BoolPort", "value": false}, "is_visible": {"customized": false, "type": "BoolPort", "value": true}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "port_category": {"customized": false, "type": "StringPort", "value": ""}, "portname": {"customized": false, "type": "StringPort", "value": "data"}, "relationships": {"customized": false, "type": "ListPort", "value": []}, "safe": {"customized": false, "type": "BoolPort", "value": false}, "select": {"customized": false, "type": "EnumPort", "value": "none"}, "send_signal_changed": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "value_type": {"customized": false, "type": "EnumPort", "value": "str"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "verbose_name": {"customized": false, "type": "StringPort", "value": null}}, "uuid": "0c3aecdb-87fb-415b-bd5f-0c641ce721c8"}, "node29": {"class": "StringConcat", "module": "neuropype.nodes.programming.StringConcat", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "separator": {"customized": false, "type": "StringPort", "value": ""}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "6c2a7f21-56b2-45fa-8b93-91d95be49e5c"}, "node3": {"class": "SeparateStreams", "module": "neuropype.nodes.formatting.SeparateStreams", "params": {"condition": {"customized": true, "type": "ComboPort", "value": "modality=='EEG'"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "ab646e1b-7482-48f0-a250-705d69dc3236"}, "node30": {"class": "ImportEDF", "module": "neuropype.nodes.file_system.ImportEDF", "params": {"cloud_account": {"customized": false, "type": "StringPort", "value": ""}, "cloud_bucket": {"customized": false, "type": "StringPort", "value": ""}, "cloud_credentials": {"customized": false, "type": "StringPort", "value": ""}, "cloud_host": {"customized": false, "type": "EnumPort", "value": "Default"}, "exclude_channels": {"customized": false, "type": "ListPort", "value": []}, "filename": {"customized": false, "type": "StringPort", "value": ""}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stim_channel": {"customized": false, "type": "StringPort", "value": ""}, "strip_modality": {"customized": false, "type": "BoolPort", "value": true}, "unit": {"customized": false, "type": "EnumPort", "value": "uV"}}, "uuid": "24305725-3f4c-4f06-8862-c54bd56fff33"}, "node31": {"class": "SpectrumPlot", "module": "neuropype.nodes.visualization.SpectrumPlot", "params": {"always_on_top": {"customized": true, "type": "BoolPort", "value": true}, "annotation_font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": true}, "autoscale": {"customized": false, "type": "BoolPort", "value": false}, "background_color": {"customized": false, "type": "StringPort", "value": "#303030"}, "colormap": {"customized": false, "type": "EnumPort", "value": "gist_rainbow"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#B0B0B0"}, "font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "initial_dims": {"customized": false, "type": "ListPort", "value": [50, 50, 1000, 800]}, "label_rotation": {"customized": false, "type": "EnumPort", "value": "horizontal"}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "line_color": {"customized": false, "type": "StringPort", "value": "white"}, "line_width": {"customized": false, "type": "FloatPort", "value": 1.25}, "max_channels": {"customized": false, "type": "IntPort", "value": 32}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "one_over_f_correction": {"customized": true, "type": "BoolPort", "value": true}, "plot_minmax": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": false, "type": "FloatPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stacked": {"customized": true, "type": "BoolPort", "value": true}, "stream": {"customized": false, "type": "StringPort", "value": null}, "stream_name": {"customized": false, "type": "AliasPort", "value": null}, "tight_layout": {"customized": false, "type": "BoolPort", "value": true}, "title": {"customized": true, "type": "StringPort", "value": "PSD_after"}, "track_window_position": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": false, "type": "EnumPort", "value": "PSD"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "x_label": {"customized": false, "type": "StringPort", "value": ""}, "x_range": {"customized": true, "type": "ListPort", "value": [0, 50]}, "y_label": {"customized": false, "type": "StringPort", "value": ""}, "y_range": {"customized": true, "type": "ListPort", "value": [0, 60]}, "zero_color": {"customized": false, "type": "StringPort", "value": "#606060"}}, "uuid": "995913ae-00cc-4791-bb20-ce1f872bda33"}, "node32": {"class": "MultitaperSpectrum", "module": "neuropype.nodes.spectral.MultitaperSpectrum", "params": {"average_over_time_window": {"customized": false, "type": "BoolPort", "value": false}, "half_bandwidth": {"customized": false, "type": "FloatPort", "value": 2.5}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nfft": {"customized": false, "type": "IntPort", "value": null}, "num_tapers": {"customized": false, "type": "IntPort", "value": null}, "onesided": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "d10402d1-2af4-4aa4-87a5-f7f508aff354"}, "node33": {"class": "MovingWindow", "module": "neuropype.nodes.signal_processing.MovingWindow", "params": {"flag_as_offline": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": false, "type": "EnumPort", "value": "seconds"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "window_length": {"customized": true, "type": "FloatPort", "value": 3.0}}, "uuid": "f51fd4b7-0675-4748-8560-24ce55269f78"}, "node34": {"class": "ToDecibels", "module": "neuropype.nodes.elementwise_math.ToDecibels", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "replace_zeros": {"customized": false, "type": "BoolPort", "value": true}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "source_measure": {"customized": false, "type": "EnumPort", "value": "auto"}, "verbose": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "b2ea620b-c0ea-420f-b92e-00c35d6578d9"}, "node35": {"class": "SpectrumPlot", "module": "neuropype.nodes.visualization.SpectrumPlot", "params": {"always_on_top": {"customized": true, "type": "BoolPort", "value": true}, "annotation_font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": true}, "autoscale": {"customized": false, "type": "BoolPort", "value": false}, "background_color": {"customized": false, "type": "StringPort", "value": "#303030"}, "colormap": {"customized": false, "type": "EnumPort", "value": "gist_rainbow"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#B0B0B0"}, "font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "initial_dims": {"customized": false, "type": "ListPort", "value": [50, 50, 1000, 800]}, "label_rotation": {"customized": false, "type": "EnumPort", "value": "horizontal"}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "line_color": {"customized": false, "type": "StringPort", "value": "white"}, "line_width": {"customized": false, "type": "FloatPort", "value": 1.25}, "max_channels": {"customized": true, "type": "IntPort", "value": 19}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "one_over_f_correction": {"customized": true, "type": "BoolPort", "value": true}, "plot_minmax": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": false, "type": "FloatPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stacked": {"customized": true, "type": "BoolPort", "value": true}, "stream": {"customized": false, "type": "StringPort", "value": null}, "stream_name": {"customized": false, "type": "AliasPort", "value": null}, "tight_layout": {"customized": false, "type": "BoolPort", "value": true}, "title": {"customized": true, "type": "StringPort", "value": "PSD_before"}, "track_window_position": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": false, "type": "EnumPort", "value": "PSD"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "x_label": {"customized": false, "type": "StringPort", "value": ""}, "x_range": {"customized": true, "type": "ListPort", "value": [0, 50]}, "y_label": {"customized": false, "type": "StringPort", "value": ""}, "y_range": {"customized": true, "type": "ListPort", "value": [0, 60]}, "zero_color": {"customized": false, "type": "StringPort", "value": "#606060"}}, "uuid": "141b25bb-7df9-4b55-8935-889467b124b5"}, "node4": {"class": "DejitterTimestamps", "module": "neuropype.nodes.utilities.DejitterTimestamps", "params": {"force_monotonic": {"customized": false, "type": "BoolPort", "value": true}, "forget_halftime": {"customized": false, "type": "FloatPort", "value": 90.0}, "max_updaterate": {"customized": false, "type": "IntPort", "value": 500}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "warmup_samples": {"customized": false, "type": "IntPort", "value": -1}}, "uuid": "f199189e-d949-4aa6-ac4f-f85ee0b524bf"}, "node5": {"class": "AssignChannelLocations", "module": "neuropype.nodes.source_localization.AssignChannelLocations", "params": {"force_override": {"customized": false, "type": "BoolPort", "value": true}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "montage": {"customized": false, "type": "StringPort", "value": ""}, "montage_type": {"customized": false, "type": "EnumPort", "value": "auto"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "6e3689bf-901d-42d1-8f37-27a1d1938fb5"}, "node6": {"class": "RemoveUnlocalizedChannels", "module": "neuropype.nodes.source_localization.RemoveUnlocalizedChannels", "params": {"metadata": {"customized": false, "type": "DictPort", "value": {}}, "protect_channels": {"customized": false, "type": "ListPort", "value": []}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "77893434-35b8-499f-8ab7-5c27c409aa12"}, "node7": {"class": "TimeSeriesPlot", "module": "neuropype.nodes.visualization.TimeSeriesPlot", "params": {"absolute_time": {"customized": false, "type": "BoolPort", "value": false}, "always_on_top": {"customized": true, "type": "BoolPort", "value": true}, "annotation_font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": true}, "autoscale": {"customized": false, "type": "BoolPort", "value": true}, "background_color": {"customized": false, "type": "StringPort", "value": "#303030"}, "colormap": {"customized": false, "type": "EnumPort", "value": "gist_rainbow"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#B0B0B0"}, "font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "initial_dims": {"customized": true, "type": "ListPort", "value": [50, 50, 500, 400]}, "label_rotation": {"customized": false, "type": "EnumPort", "value": "horizontal"}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "line_color": {"customized": false, "type": "StringPort", "value": "white"}, "line_width": {"customized": false, "type": "FloatPort", "value": 1.25}, "marker_color": {"customized": false, "type": "Port", "value": "darkorange"}, "max_channels": {"customized": false, "type": "IntPort", "value": 32}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nans_as_zero": {"customized": false, "type": "BoolPort", "value": false}, "no_concatenate": {"customized": false, "type": "BoolPort", "value": false}, "override_srate": {"customized": false, "type": "FloatPort", "value": null}, "plot_markers": {"customized": false, "type": "BoolPort", "value": false}, "plot_minmax": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": false, "type": "FloatPort", "value": 1.0}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stream": {"customized": false, "type": "StringPort", "value": null}, "stream_name": {"customized": false, "type": "AliasPort", "value": null}, "tight_layout": {"customized": false, "type": "BoolPort", "value": true}, "time_range": {"customized": false, "type": "FloatPort", "value": 5.0}, "title": {"customized": true, "type": "StringPort", "value": "Before Filtering"}, "track_window_position": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "x_axis": {"customized": false, "type": "ComboPort", "value": "time"}, "x_label": {"customized": false, "type": "StringPort", "value": ""}, "y_axis": {"customized": false, "type": "ComboPort", "value": "space"}, "y_label": {"customized": false, "type": "StringPort", "value": ""}, "zero_color": {"customized": false, "type": "StringPort", "value": "#606060"}, "zeromean": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "78d7ef23-8590-4289-b8a3-958444cbec19"}, "node8": {"class": "IIRFilter", "module": "neuropype.nodes.signal_processing.IIRFilter", "params": {"axis": {"customized": false, "type": "ComboPort", "value": "time"}, "design": {"customized": false, "type": "EnumPort", "value": "butter"}, "frequencies": {"customized": true, "type": "ListPort", "value": [0.25, 1, 45, 50]}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "mode": {"customized": false, "type": "EnumPort", "value": "bandpass"}, "offline_filtfilt": {"customized": false, "type": "BoolPort", "value": false}, "order": {"customized": true, "type": "IntPort", "value": 0}, "pass_loss": {"customized": false, "type": "FloatPort", "value": 3.0}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stop_atten": {"customized": true, "type": "FloatPort", "value": 40.0}}, "uuid": "b8ba0caa-28cc-4274-9844-dc9206adf577"}, "node9": {"class": "Detrend", "module": "neuropype.nodes.signal_processing.Detrend", "params": {"axis": {"customized": false, "type": "ComboPort", "value": "time"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "method": {"customized": false, "type": "EnumPort", "value": "linear"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "adc33127-f058-4275-a8c1-6b773d2463f0"}}, "version": 1.1}</patch>
</scheme>
