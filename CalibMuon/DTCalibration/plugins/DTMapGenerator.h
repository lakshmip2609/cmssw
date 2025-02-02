#ifndef DTMapGenerator_H
#define DTMapGenerator_H

/** \class DTMapGenerator
 *  Class which creates a textual map of the hardware channels 
 *  in the software detIds
 *  \author G. Cerminara S. Bolognesi - INFN Torino
 */

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "DataFormats/MuonDetId/interface/DTWireId.h"

#include <string>
#include <set>

class DTMapGenerator : public edm::one::EDAnalyzer<> {
public:
  /// Constructor
  DTMapGenerator(const edm::ParameterSet& pset);

  /// Destructor
  ~DTMapGenerator() override;

  // Operations

  void beginJob() override {}

  void analyze(const edm::Event& event, const edm::EventSetup& setup) override {}

  void endJob() override;

protected:
private:
  //Check if the wire exists in the channels list :
  //(/afs/cern.ch/cms/Physics/muon/CMSSW/DT/channelsMaps/existing_channels.txt)
  bool checkWireExist(
      const std::set<DTWireId>& wireMap, int wheel, int station, int sector, int sl, int layer, int wire);

  //file name with the output map
  std::string outputMapName;
  //file name with the input base map (DDU,ROS -> Wheel,Sector,Chamber)
  std::string inputMapName;
  //rosType = 8 for commissioning, 25 otherwise
  int rosType;
};
#endif
