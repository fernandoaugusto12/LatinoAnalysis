Trigger = {


# --------------------------- Full2018 ---------------------------------

   # https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmV2018Analysis
   # Using lumi obtained with normtag
   # Full 2018 lumi --> 58.826
   
   # export PATH=$HOME/.local/bin:/afs/cern.ch/cms/lumi/brilconda-1.1.7/bin:$PATH
   # brilcalc lumi -u /fb -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt
        # TODO: still Latino, edit to Mono
        'Full2018'  :  {  
                          # Full 2018 
                          1  :  { 'begin' : 315252 , 'end' : 325175 , 'lumi' : 58.826 ,
                                  # FIXME: UPdate with 2018 values
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'DoubleEleLegLowPt' : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'SingleEle'         : 'Full2017/Ele35_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017B.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017B.txt' ,
                                                'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017B.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017B.txt',
                                                'MuEleLegLowPt'     : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                              } ,
                                  # FIXME: UPdate with 2018 values
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017/DZEff_em.txt' } ,
                                              } ,
                                  # Electron HLT Zvtx Efficiency Scale Factor: 0.934+-0.005
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele32_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu24'] ,
                                                'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele32_WPTight_Gsf'] ,
                                              } ,

                                  },
                          },


# --------------------------- Full2017 ---------------------------------


#ERA	       Absolute Run Number	
#                From Run To Run  Lumi (/fb)  Run Preiod	
#Run2017B	297020	299329	   4.794      -> 1
#Run2017C	299337	302029	   9.633      -> 2
#Run2017D	302030	303434	   4.248      -> 3
#Run2017E	303435	304826	   9.315      -> 4 
#Run2017F	304911	306462	  13.540      -> 5
# TOTAL                           41.529

#brilcalc lumi --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -i /afs/cern.ch/cms/CAF
#/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt -u /fb
# --begin 299337 --end  302029

        'Full2017v2'  :  {  
                          # Run B 
                          #TODO upload eff, check if names for MC = names DATA
                          1  :  { 'begin' : 297020 , 'end' : 299329 , 'lumi' : 4.793 ,
                                  'LegEff' :  { #'DoubleEleLegHigPt' : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                #'DoubleEleLegLowPt' : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'SingleEle'         : 'Full2017/Ele35_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017B.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017B.txt' ,
                                                'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017B.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017B.txt',
                                                'MuEleLegLowPt'     : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017B.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'pt1:pt2' : 'Full2017/DZEff_me.txt' } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017/DZEff_em.txt' } ,
                                              } ,
                                  # Electron HLT Zvtx Efficiency Scale Factor: 0.934+-0.005
                                  'GlEff'  :  { 'DoubleEle' : [0.934,0.005],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [0.934,0.005],
                                                'EleMu'     : [0.934,0.005],
                                                'SingleEle' : [0.934,0.005],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_MW'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                #'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,

                                },

                          # Run C
                          #TODO upload eff, check if names for MC = names DATA
                          2  :  { 'begin' : 299337 , 'end' : 302029 , 'lumi' : 9.633 ,
                                  'LegEff' :  { #'DoubleEleLegHigPt' : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                #'DoubleEleLegLowPt' : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017CD.txt' ,
                                                'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                'MuEleLegLowPt'     : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegHigPt'     : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'nvtx'    : 'Full2017/DZEff_mm.txt' } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'nvtx'    : 'Full2017/DZEff_em.txt' } ,
                                              } ,
                                  # Electron HLT Zvtx Efficiency Scale Factor: 0.992+-0.001
                                  'GlEff'  :  { 'DoubleEle' : [0.992,0.001],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [0.992,0.001],
                                                'EleMu'     : [0.992,0.001],
                                                'SingleEle' : [0.992,0.001],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  { 
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_MW'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                #'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },

                          # Run2017D       302030  303434     4.248
                          #TODO upload eff, check if names for MC = names DATA
                          3  :  { 'begin' : 302030 , 'end' : 303434  , 'lumi' : 4.248 ,
                                  'LegEff' :  { #'DoubleEleLegHigPt' : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                #'DoubleEleLegLowPt' : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                #'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                #'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                #'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017CD.txt' ,
                                                #'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                #'MuEleLegLowPt'     : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                #'EleMuLegHigPt'     : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                #'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'value'   : [1.0,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0,0.0] } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu37_Ele27_CaloIdL_MW', 'HLT_Mu27_Ele37_CaloIdL_MW'] ,
                                                'DoubleMu'  : [ 'HLT_Mu37_TkMu27'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle25_CaloIdL_MW'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                #'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                #'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                #'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                #'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },

                          # Run2017E       303435  304826     9.315
                          #TODO upload eff, check if names for MC = names DATA
                          4  :  { 'begin' : 303435 , 'end' : 304826  , 'lumi' : 9.315 ,
                                  'LegEff' :  { #'DoubleEleLegHigPt' : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                #'DoubleEleLegLowPt' : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                #'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                #'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                #'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017CD.txt' ,
                                                #'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                #'MuEleLegLowPt'     : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                #'EleMuLegHigPt'     : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                #'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'value'   : [1.0,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0,0.0] } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu37_Ele27_CaloIdL_MW', 'HLT_Mu27_Ele37_CaloIdL_MW'] ,
                                                'DoubleMu'  : [ 'HLT_Mu37_TkMu27'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle25_CaloIdL_MW'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                #'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                #'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                #'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                #'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },


                          # Run2017F       304911  306462    13.540
                          #TODO upload eff, check if names for MC = names DATA
                          5  :  { 'begin' : 304911 , 'end' : 306462  , 'lumi' : 13.540 ,
                                  'LegEff' :  { #'DoubleEleLegHigPt' : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                #'DoubleEleLegLowPt' : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                'SingleEle'         : 'Full2017/Ele35_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                #'DoubleMuLegHigPt'  : 'Full2017/Mu17_Mu8_leg1_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                #'DoubleMuLegLowPt'  : 'Full2017/Mu17_Mu8_leg2_pt_eta_Iso_efficiency_Run2017CD.txt' ,
                                                #'SingleMu'          : 'Full2017/IsoMu27_pt_eta_efficiency_Run2017CD.txt' ,
                                                #'MuEleLegHigPt'     : 'Full2017/Mu23_pt_eta_efficiency_withSys_Run2017CDE.txt',
                                                #'MuEleLegLowPt'     : 'Full2017/Ele23_Ele12_leg2_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                #'EleMuLegHigPt'     : 'Full2017/Ele23_Ele12_leg1_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                                #'EleMuLegLowPt'     : 'Full2017/Mu12_pt_eta_efficiency_withSys_Run2017CDE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0,0.0] } ,
                                                'DoubleMu'  : { 'value'   : [1.0,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0,0.0] } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code?'
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu37_Ele27_CaloIdL_MW', 'HLT_Mu27_Ele37_CaloIdL_MW'] ,
                                                'DoubleMu'  : [ 'HLT_Mu37_TkMu27'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle25_CaloIdL_MW'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                  'MC'     :  {
                                                #'EleMu'     : [ 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL', 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ'] ,
                                                #'DoubleMu'  : [ 'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ'] ,
                                                #'SingleMu'  : [ 'HLT_IsoMu27'] ,
                                                #'DoubleEle' : [ 'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL'] ,
                                                'SingleEle' : [ 'HLT_Ele35_WPTight_Gsf'] ,
                                              } ,
                                },



                       },   

# --------------------------- Full2016 ---------------------------------

#   ------------------------------
#     dataset | from run | to run
#   ----------+----------+--------
#    Run2016B |   272007 | 275376  -> 5.788 /fb                             f_BCDEF = 0.294
#    Run2016C |   275657 | 276283  -> 2.573 /fb                             f_BCDEF = 0.130
#    Run2016D |   276315 | 276811  -> 4.248 /fb                             f_BCDEF = 0.215
#    Run2016E |   276831 | 277420  -> 4.009 /fb                             f_BCDEF = 0.203
#    Run2016F |   277772 | 278808  -> 3.102 /fb -> B+C+D+E+F : 19.720 / fb  f_BCDEF = 0.157
#    Run2016G |   278820 | 280385  -> 7.540 /fb
#    Run2016H |   280919 |         -> 8.606 /fb --> G+H: 16.146 /fb
#    Total lumi: 35.867 /fb (brilcalc lumi --normtag /afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt -u /fb)
#   ------------------------------

        # TODO: still Latino, edit to Mono
        'Full2016v2'  :  { 
                          # Lower Muon efficiency at begin of 2016 + L1 EMTF Bug ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          1  :  { 'begin' : 273158 , 'end' : 274094 , 'lumi' :  0.616 ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunB.txt' ,
                                                'DoubleEleLegLowPt' : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunB.txt' ,
                                                'SingleEle'         : None ,
                                                'DoubleMuLegHigPt'  : 'monoHiggs/2016/Mu30_TkMu11_leg1_pt_eta_nominal_withSys_efficiency_RunB.txt' ,
                                                'DoubleMuLegLowPt'  : 'monoHiggs/2016/Mu30_TkMu11_leg2_pt_eta_nominal_withSys_efficiency_RunB.txt',
                                                'SingleMu'          : 'monoHiggs/2016/Mu50_pt_eta_nominal_withSys_efficiency_RunB.txt' ,
                                                'MuEleLegHigPt'     : 'monoHiggs/2016/Mu33_Ele33_emu_legMu_pt_eta_nominal_withSys_efficiency_RunB.txt' ,
                                                'MuEleLegLowPt'     : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunB.txt' ,
                                                'EleMuLegHigPt'     : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunB.txt' ,
                                                'EleMuLegLowPt'     : 'monoHiggs/2016/Mu33_Ele33_emu_legMu_pt_eta_nominal_withSys_efficiency_RunB.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0   ,0.0] } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0   ,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0   ,0.0] } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  True , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu30_TkMu11'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'] ,
                                                'SingleEle' : [ None ] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu30_TkMu11'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'] ,
                                                'SingleEle' : [ None ] ,
                                              } ,

                                },
                          # L1 EMFT Bug ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          2  :  { 'begin' : 274095 , 'end' : 277165 , 'lumi' : 15.005  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunC.txt' ,
                                                'DoubleEleLegLowPt' : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunC.txt' ,
                                                'SingleEle'         : None ,
                                                'DoubleMuLegHigPt'  : 'monoHiggs/2016/Mu30_TkMu11_leg1_pt_eta_nominal_withSys_efficiency_RunC.txt' ,
                                                'DoubleMuLegLowPt'  : 'monoHiggs/2016/Mu30_TkMu11_leg2_pt_eta_nominal_withSys_efficiency_RunC.txt',
                                                'SingleMu'          : 'monoHiggs/2016/Mu50_pt_eta_nominal_withSys_efficiency_RunC.txt' ,
                                                'MuEleLegHigPt'     : 'monoHiggs/2016/Mu33_Ele33_emu_legMu_pt_eta_nominal_withSys_efficiency_RunC.txt' ,
                                                'MuEleLegLowPt'     : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunC.txt' ,
                                                'EleMuLegHigPt'     : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunC.txt' ,
                                                'EleMuLegLowPt'     : 'monoHiggs/2016/Mu33_Ele33_emu_legMu_pt_eta_nominal_withSys_efficiency_RunC.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0   ,0.0] } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0   ,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0   ,0.0] } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  True , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu30_TkMu11'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'] ,
                                                'SingleEle' : [ None ] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu30_TkMu11'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'] ,
                                                'SingleEle' : [ None ] ,
                                              } ,
                                },
                          # Run>=277166: L1 EMTF Bug fixed ( https://twiki.cern.ch/twiki/bin/view/CMS/EndcapHighPtMuonEfficiencyProblem )
                          3  :  { 'begin' : 277166 , 'end' : 278272 , 'lumi' : 2.059  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunD.txt' ,
                                                'DoubleEleLegLowPt' : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunD.txt' ,
                                                'SingleEle'         : None ,
                                                'DoubleMuLegHigPt'  : 'monoHiggs/2016/Mu30_TkMu11_leg1_pt_eta_nominal_withSys_efficiency_RunD.txt' ,
                                                'DoubleMuLegLowPt'  : 'monoHiggs/2016/Mu30_TkMu11_leg2_pt_eta_nominal_withSys_efficiency_RunD.txt',
                                                'SingleMu'          : 'monoHiggs/2016/Mu50_pt_eta_nominal_withSys_efficiency_RunD.txt' ,
                                                'MuEleLegHigPt'     : 'monoHiggs/2016/Mu33_Ele33_emu_legMu_pt_eta_nominal_withSys_efficiency_RunD.txt' ,
                                                'MuEleLegLowPt'     : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunD.txt' ,
                                                'EleMuLegHigPt'     : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunD.txt' ,
                                                'EleMuLegLowPt'     : 'monoHiggs/2016/Mu33_Ele33_emu_legMu_pt_eta_nominal_withSys_efficiency_RunD.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0   ,0.0] } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0   ,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0   ,0.0] } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu30_TkMu11'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'] ,
                                                'SingleEle' : [ None ] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu30_TkMu11'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'] ,
                                                'SingleEle' : [ None ] ,
                                              } ,
                                },
                          # Run>=278273: Switch to DZ version of E-Mu triggers
                          # OLD: 4  :  { 'begin' : 278273 , 'end' : 281612 , 'lumi' : 9.818  ,
                          4  :  { 'begin' : 278273 , 'end' : 278808 , 'lumi' : 2.041  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunE.txt' ,
                                                'DoubleEleLegLowPt' : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunE.txt' ,
                                                'SingleEle'         : None ,
                                                'DoubleMuLegHigPt'  : 'monoHiggs/2016/Mu30_TkMu11_leg1_pt_eta_nominal_withSys_efficiency_RunE.txt' ,
                                                'DoubleMuLegLowPt'  : 'monoHiggs/2016/Mu30_TkMu11_leg2_pt_eta_nominal_withSys_efficiency_RunE.txt',
                                                'SingleMu'          : 'monoHiggs/2016/Mu50_pt_eta_nominal_withSys_efficiency_RunE.txt' ,
                                                'MuEleLegHigPt'     : 'monoHiggs/2016/Mu33_Ele33_emu_legMu_pt_eta_nominal_withSys_efficiency_RunE.txt' ,
                                                'MuEleLegLowPt'     : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunE.txt' ,
                                                'EleMuLegHigPt'     : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunE.txt' ,
                                                'EleMuLegLowPt'     : 'monoHiggs/2016/Mu33_Ele33_emu_legMu_pt_eta_nominal_withSys_efficiency_RunE.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0   ,0.0] } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0   ,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0   ,0.0] } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu30_TkMu11'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'] ,
                                                'SingleEle' : [ None ] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu30_TkMu11'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'] ,
                                                'SingleEle' : [ None ] ,
                                              } ,
                                },
                          # No change of trigger, same as period 4
                          # END of HIP problem -> Muon ID/ISO SF change
                          #    Run2016G |   278820 | 280385
                          #    Run2016H |   280919 |
                          5  :  { 'begin' : 278820 , 'end' : 281612 , 'lumi' : 7.540  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunF.txt' ,
                                                'DoubleEleLegLowPt' : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunF.txt' ,
                                                'SingleEle'         : None ,
                                                'DoubleMuLegHigPt'  : 'monoHiggs/2016/Mu30_TkMu11_leg1_pt_eta_nominal_withSys_efficiency_RunF.txt' ,
                                                'DoubleMuLegLowPt'  : 'monoHiggs/2016/Mu30_TkMu11_leg2_pt_eta_nominal_withSys_efficiency_RunF.txt',
                                                'SingleMu'          : 'monoHiggs/2016/Mu50_pt_eta_nominal_withSys_efficiency_RunF.txt' ,
                                                'MuEleLegHigPt'     : 'monoHiggs/2016/Mu33_Ele33_emu_legMu_pt_eta_nominal_withSys_efficiency_RunF.txt' ,
                                                'MuEleLegLowPt'     : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunF.txt' ,
                                                'EleMuLegHigPt'     : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunF.txt' ,
                                                'EleMuLegLowPt'     : 'monoHiggs/2016/Mu33_Ele33_emu_legMu_pt_eta_nominal_withSys_efficiency_RunF.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0   ,0.0] } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0   ,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0   ,0.0] } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu30_TkMu11'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'] ,
                                                'SingleEle' : [ None ] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu30_TkMu11'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'] ,
                                                'SingleEle' : [ None ] ,
                                              } ,
                                },
                          # Run>=281613: Switch to DZ version of Double Mu triggersA : Lumi 8.606 - 0.860 = 7.746 (to accomodate space for pseudo period 7)
                          6  :  { 'begin' : 281613 , 'end' : 284042 , 'lumi' : 7.746  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunG.txt' ,
                                                'DoubleEleLegLowPt' : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunG.txt' ,
                                                'SingleEle'         : None ,
                                                'DoubleMuLegHigPt'  : 'monoHiggs/2016/Mu30_TkMu11_leg1_pt_eta_nominal_withSys_efficiency_RunG.txt' ,
                                                'DoubleMuLegLowPt'  : 'monoHiggs/2016/Mu30_TkMu11_leg2_pt_eta_nominal_withSys_efficiency_RunG.txt',
                                                'SingleMu'          : 'monoHiggs/2016/Mu50_pt_eta_nominal_withSys_efficiency_RunG.txt' ,
                                                'MuEleLegHigPt'     : 'monoHiggs/2016/Mu33_Ele33_emu_legMu_pt_eta_nominal_withSys_efficiency_RunG.txt' ,
                                                'MuEleLegLowPt'     : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunG.txt' ,
                                                'EleMuLegHigPt'     : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunG.txt' ,
                                                'EleMuLegLowPt'     : 'monoHiggs/2016/Mu33_Ele33_emu_legMu_pt_eta_nominal_withSys_efficiency_RunG.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0   ,0.0] } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0   ,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0   ,0.0] } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu30_TkMu11'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'] ,
                                                'SingleEle' : [ None ] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu30_TkMu11'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'] ,
                                                'SingleEle' : [ None ] ,
                                              } ,
                                }, 
                          # Run>=281613: Switch to DZ version of Double Mu triggers ... Few LS where HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL is seeded by L1_Mu23_EG10 
                          # Attributed to last run as a trick to switch to the lower efficiency
                          7  :  { 'begin' : 284043 , 'end' : 284044 , 'lumi' : 0.860  ,
                                  'LegEff' :  { 'DoubleEleLegHigPt' : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunH.txt' ,
                                                'DoubleEleLegLowPt' : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunH.txt' ,
                                                'SingleEle'         : None ,
                                                'DoubleMuLegHigPt'  : 'monoHiggs/2016/Mu30_TkMu11_leg1_pt_eta_nominal_withSys_efficiency_RunH.txt' ,
                                                'DoubleMuLegLowPt'  : 'monoHiggs/2016/Mu30_TkMu11_leg2_pt_eta_nominal_withSys_efficiency_RunH.txt',
                                                'SingleMu'          : 'monoHiggs/2016/Mu50_pt_eta_nominal_withSys_efficiency_RunH.txt' ,
                                                'MuEleLegHigPt'     : 'monoHiggs/2016/Mu33_Ele33_emu_legMu_pt_eta_nominal_withSys_efficiency_RunH.txt' ,
                                                'MuEleLegLowPt'     : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunH.txt' ,
                                                'EleMuLegHigPt'     : 'monoHiggs/2016/DoubleEle33_GsfTrkIdVL_leg_pt_eta_nominal_withSys_efficiency_RunH.txt' ,
                                                'EleMuLegLowPt'     : 'monoHiggs/2016/Mu33_Ele33_emu_legMu_pt_eta_nominal_withSys_efficiency_RunH.txt' ,
                                              } ,
                                  'DZEff'  :  { 
                                                'DoubleEle' : { 'value'   : [1.0   ,0.0] } ,
                                                'DoubleMu'  : { 'value'   : [1.0   ,0.0] } ,
                                                'MuEle'     : { 'value'   : [1.0   ,0.0] } ,
                                                'EleMu'     : { 'value'   : [1.0   ,0.0] } ,
                                              } ,
                                  'GlEff'  :  { 'DoubleEle' : [1.0  ,0.   ],
                                                'DoubleMu'  : [1.0  ,0.   ],
                                                'MuEle'     : [1.0  ,0.   ],
                                                'EleMu'     : [1.0  ,0.   ],
                                                'SingleEle' : [1.0  ,0.   ],
                                                'SingleMu'  : [1.0  ,0.   ],
                                              } ,
                                  'EMTFBug':  False , 
                                  #'trkSFMu':  [ 1.00 , 1.00 , 1.00 ] , # tracker SF_muons [ cent , up , down ] --> Moved to ID/Iso code
                                  'DATA'   :  {
                                                'EleMu'     : [ 'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu30_TkMu11'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'] ,
                                                'SingleEle' : [ None ] ,
                                              } ,
                                  'MC'     :  {
                                                'EleMu'     : [ 'HLT_Mu33_Ele33_CaloIdL_GsfTrkIdVL'] ,
                                                'DoubleMu'  : [ 'HLT_Mu30_TkMu11'] ,
                                                'SingleMu'  : [ 'HLT_Mu50'] ,
                                                'DoubleEle' : [ 'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL'] ,
                                                'SingleEle' : [ None ] ,
                                              } ,
                                },
        
                       }
}

Trigger['Full2016v4'] = Trigger['Full2016v2'] 
Trigger['Full2017v4'] = Trigger['Full2017v2'] 
Trigger['Full2018v4'] = Trigger['Full2018'] 


NewVar_MC_dict = {
   'F': [
         'MHTriggerEffWeight_2l',
         'MHTriggerEffWeight_2l_u',
         'MHTriggerEffWeight_2l_d',
         'MHTriggerEffWeight_3l',
         'MHTriggerEffWeight_3l_u',
         'MHTriggerEffWeight_3l_d',
         'MHTriggerEffWeight_4l',
         'MHTriggerEffWeight_4l_u',
         'MHTriggerEffWeight_4l_d',
         'MHTriggerEffWeight_sngEl',
         'MHTriggerEffWeight_sngMu',
         'MHTriggerEffWeight_dblEl',
         'MHTriggerEffWeight_dblMu',
         'MHTriggerEffWeight_ElMu',
        ],
   'I': [
         #'MHTriggerEmulator',
         #'EMTFbug_veto',
         #'run_period',
         'MHTrigger_sngEl',
         'MHTrigger_sngMu',
         'MHTrigger_dblEl',
         'MHTrigger_dblMu',
         'MHTrigger_ElMu'
         #'metFilter'
        ]        
}

NewVar_DATA_dict = {
   'F': [
        ],
   'I': [
         #'EMTFbug_veto',
         #'run_period',
         'MHTrigger_sngEl',
         'MHTrigger_sngMu',
         'MHTrigger_dblEl',
         'MHTrigger_dblMu',
         'MHTrigger_ElMu'
         #'metFilter'
        ]        
}



if __name__ == '__main__':
   for key in Trigger:
      print(Trigger[key])
   print(Trigger['Full2016'][6]['MC'])

