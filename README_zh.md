<h1 align="center">OAbuddy</h1>

<p align="center"><em>
公开海洋和大气数据集集合
</em></p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/mhuia/OAbuddy" alt="Last Commit">
  <img src="https://img.shields.io/github/issues/mhuia/OAbuddy" alt="Open Issues">
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen" alt="Contributions Welcome">
  <img src="https://github.com/mhuia/OABuddy/actions/workflows/readme-check.yml/badge.svg" alt="Check">
</p>

<p align="center">
  <a href="./README.md">English</a> | <a>简体中文</a>
</p>

<!-- TODO: 标准化术语 -->

## 📋 目录
- [📊 常用数据集](#-常用数据集)
- [🗃️ 其他数据集](#️-其他数据集)
- [🔧 常用工具](#-常用工具)
- [🌐 数值模式](#-数值模式)
- [🤖 大模型](#-海洋气象大模型)
- [🤝 如何贡献](#-如何贡献)
- [📜 开源许可](#-开源许可)

<br>

## 📊 常用数据集:

| 数据集名称 | 机构 | 相关信息 |
| ---------- | ---- | -------- |
| ECMWF Reanalysis v5 (**ERA5**) hourly data on single levels from 1940 to present | [Climate Data Store](https://cds.climate.copernicus.eu/) | [Description](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview) <br> [Download](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) <br> [Citation](https://doi.org/10.24381/cds.adbb2d47) |
| **ERA-Interim** (from 1979-01 to 2019-09) | [NSF NCAR](https://ncar.ucar.edu/) | [Description](https://climatedataguide.ucar.edu/climate-data/era-interim) <br> [Download](https://climatedataguide.ucar.edu/climate-data/era-interim) <br> [How to cite](https://climatedataguide.ucar.edu/climate-data/era-interim) |
| Global Ocean Physics Reanalysis (**GLORYS**12V1) | [Copernicus Marine Data Store](https://data.marine.copernicus.eu/products) | [Description](https://data.marine.copernicus.eu/product/GLOBAL_MULTIYEAR_PHY_001_030/description) <br> [Download](https://data.marine.copernicus.eu/product/GLOBAL_MULTIYEAR_PHY_001_030/services) | [Citation](https://doi.org/10.48670/moi-00021) <br> [How to cite](https://help.marine.copernicus.eu/en/articles/4444611-how-to-cite-copernicus-marine-products-and-services) |
| Optimum Interpolation Sea Surface Temperature (**OISST**) | [NOAA](https://www.ncei.noaa.gov/) [NCEI](https://www.ncei.noaa.gov/) | [Description](https://www.ncei.noaa.gov/products/optimum-interpolation-sst) <br> [Download](https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.highres.html) | [Citation](https://doi.org/10.1175/JCLI-D-20-0166.1) |
| Results of MITgcm on LLC (e.g. **LLC4320**, **LLC2160**) | [NASA Data Portal](https://data.nas.nasa.gov/) | [Description](https://www.nature.com/articles/s41467-018-02983-w) <br> [Download](https://data.nas.nasa.gov/ecco/data.php?dir=/eccodata/llc_4320) | [Citation](https://doi.org/10.1038/s41467-018-02983-w) |
| **MODIS** Aqua/Terra (L3/L4) | [Ocean Color](https://oceancolor.gsfc.nasa.gov/) | [Description](https://modis.gsfc.nasa.gov/) <br> [Download](https://oceandata.sci.gsfc.nasa.gov/l3/) | [How to cite](https://oceancolor.gsfc.nasa.gov/resources/how-to-cite/) |
| **AVHRR** Pathfinder **SST** (1981-2023) | [NOAA](https://www.noaa.gov/) [NCEI](https://www.ncei.noaa.gov/) | [Description](https://www.ncei.noaa.gov/products/avhrr-pathfinder-sst) <br>[ Download](https://www.ncei.noaa.gov/data/oceans/pathfinder/Version5.3/L3C/) <br> [Citation](https://doi.org/10.7289/v52j68xx) |
| Global Drifter Program (**GDP**) Drifer Data | [NOAA](https://www.noaa.gov/) [AOML](https://www.aoml.noaa.gov/) [PhOD](https://www.aoml.noaa.gov/physical-oceanography-division/) | [Description](https://www.aoml.noaa.gov/phod/gdp/data.php) |
| Global **Argo** Data Repository | [NOAA](https://www.ncei.noaa.gov/) [NCEI](https://www.ncei.noaa.gov/) | [Description](https://www.ncei.noaa.gov/products/global-argo-data-repository) <br> Download <br> [How to cite](https://argo.ucsd.edu/data/acknowledging-argo/) |
| **Argo** data sources | [Argo](https://argo.ucsd.edu/) | [Description](https://argo.ucsd.edu/) <br> [Download](https://argo.ucsd.edu/data/) | [Cition](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2020.00700/full) <br> [How to cite](https://argo.ucsd.edu/data/acknowledging-argo/) |
| Global Temperature and Salinity Profile Programme (**GTSPP**) | [NOAA](https://www.ncei.noaa.gov/) [NCEI](https://www.ncei.noaa.gov/) | [Description](https://www.ncei.noaa.gov/products/global-temperature-and-salinity-profile-programme) <br> [Download](https://www.ncei.noaa.gov/products/global-temperature-and-salinity-profile-programme) |[Citation](https://www.ncei.noaa.gov/products/global-temperature-and-salinity-profile-programme)
| World Ocean Database (**WOD**) | [NOAA](https://www.ncei.noaa.gov/) [NCEI](https://www.ncei.noaa.gov/) | [Description](https://www.ncei.noaa.gov/products/world-ocean-database) <br> [Download](https://www.ncei.noaa.gov/products/world-ocean-database) <br> [Citation](https://www.ncei.noaa.gov/products/world-ocean-database)
| World Ocean Atlas (**WOA**) | [NOAA](https://www.ncei.noaa.gov/) [NCEI](https://www.ncei.noaa.gov/) | [Description](https://www.ncei.noaa.gov/products/world-ocean-atlas) <br> [Download](https://www.ncei.noaa.gov/products/world-ocean-atlas) <br> [Citation](https://www.ncei.noaa.gov/products/world-ocean-atlas)| Modern-Era Retrospective analysis for Research and Applications, Version 2 (**MERRA-2**) | [NASA GMAO](https://gmao.gsfc.nasa.gov/) | [Description](https://gmao.gsfc.nasa.gov/gmao-products/merra-2/) <br> [Download](https://disc.gsfc.nasa.gov/datasets?project=MERRA-2) <br> [How to cite](https://gmao.gsfc.nasa.gov/gmao-products/merra-2/citing-merra-2-data_merra-2/)
| NCEP Global Ocean Data Assimilation System (**GODAS**) | [NOAA NCEP CPC](https://www.cpc.ncep.noaa.gov/) | [Description](https://www.cpc.ncep.noaa.gov/products/GODAS/) <br> [Download](https://www.psl.noaa.gov/data/gridded/data.godas.html) <br> [How to cite](https://www.psl.noaa.gov/data/gridded/data.godas.html)| Estimated state of ocean for climate research Version:06a (**ESTOC**) | [JAMSTEC](https://www.jamstec.go.jp/e/) | [Description](https://www.godac.jamstec.go.jp/estoc/e/description/06a.html) <br> [Download](https://www.godac.jamstec.go.jp/jagdas/catalog/estoc/catalog.html) <br> [How to cite](https://www.godac.jamstec.go.jp/estoc/e/description/06a.html)| 
**SODA**: Simple Ocean Data Assimilation | [NSF NCAR](https://ncar.ucar.edu/) | [Description](https://climatedataguide.ucar.edu/climate-data/soda-simple-ocean-data-assimilation) <br> [Download](https://dsrs.atmos.umd.edu/DATA/) <br> [How to cite](https://climatedataguide.ucar.edu/climate-data/soda-simple-ocean-data-assimilation)| 
Global Ocean Ensemble Physics Reanalysis (**GOEPR**) | [Copernicus Marine Data Store](https://data.marine.copernicus.eu/products) | [Description](https://data.marine.copernicus.eu/product/GLOBAL_MULTIYEAR_PHY_ENS_001_031/description) <br> [Download](https://data.marine.copernicus.eu/product/GLOBAL_MULTIYEAR_PHY_ENS_001_031/services) <br> [Citation](https://doi.org/10.48670/moi-00024) <br> [How to cite](https://help.marine.copernicus.eu/en/articles/4444611-how-to-cite-copernicus-marine-products-and-services)| 
NCEP **FNL** Operational Model Global Tropospheric Analyses, continuing from July 1999 | [NSF NCAR](https://ncar.ucar.edu/) | [Description](https://gdex.ucar.edu/datasets/d083002/) <br> [Download](https://gdex.ucar.edu/datasets/d083002/dataaccess/#) <br> [Citation](https://gdex.ucar.edu/datasets/d083002/citation/#) |
| **GHRSST** Level 4 MUR Global Foundation Sea Surface Temperature Analysis (v4.1) (GDS versions 1 and 2) (daily, from 2002-06-01 to 2023-03-15) | [NOAA](https://www.ncei.noaa.gov/) [NCEI](https://www.ncei.noaa.gov/) | [Description](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:GHRSST-MUR-JPL-L4-GLOB) <br> [Download](https://www.ncei.noaa.gov/thredds-ocean/catalog/ghrsst/L4/GLOB/JPL/MUR/catalog.html) <br> [How to cite](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:GHRSST-MUR-JPL-L4-GLOB) |
| WAVEWATCH III | [NOAA/NCEP](https://www.weather.gov/ncep/) | [Home](https://polar.ncep.noaa.gov/waves/index.php?) <br> [Description](https://polar.ncep.noaa.gov/waves/wavewatch/) <br> [Data Access](https://polar.ncep.noaa.gov/waves/download2.shtml?) <br> [How to cite](https://github.com/NOAA-EMC/WW3/wiki/FAQs-page#how-to-cite-wavewatch-iii) |
| Japanese Reanalysis (**JRA-25**, **DSJRA-55**, **JRA-55**, **JRA-3Q**) | [気象庁](https://www.jma.go.jp/jma/index.html) | [Project Page](https://www.data.jma.go.jp/jra/html/index.html) <br> • [JRA-25](https://www.data.jma.go.jp/jra/html/JRA-25/index_en.html) <br> • [DSJRA-55](https://www.data.jma.go.jp/jra/html/DSJRA-55/index_en.html) <br> • [JRA-55](https://www.data.jma.go.jp/jra/html/JRA-55/index_en.html) <br> • [JRA-3Q](https://www.data.jma.go.jp/jra/html/JRA-3Q/index_en.html) |
| Coupled Model Intercomparison Project (**CMIP**) | - | [Description](https://wcrp-cmip.org/) |
| High Resolution Model Intercomparison Project (**HighResMIP**) | [HighResMIP team](https://highresmip.org/about/committee/) | [Description](https://highresmip.org/) |

<br>

## 🗃️ 其他数据集:

| 数据集名称 | 机构 | 相关信息 |
| ---------- | ---- | -------- |
| The Global **Seamount** Database | - |[Description](https://www.soest.hawaii.edu/PT/SMTS/main.html) <br> [Download](https://www.soest.hawaii.edu/PT/SMTS/main.html) <br> [Citation](http://dx.doi.org/10.1111/j.1365-246X.2011.05076.x) |
| ETOPO Global Relief Model (**ETOPO 2022**) | [NOAA NCEI](https://www.ncei.noaa.gov/) | [Description](https://www.ncei.noaa.gov/products/etopo-global-relief-model) | [Download](https://data.noaa.gov/metaview/page?xml=NOAA/NESDIS/NGDC/MGG/DEM//iso/xml/etopo_2022.xml&view=getDataView&header=none) | [How to cite](https://www.ncei.noaa.gov/products/etopo-global-relief-model) |
| Gridded Bathymetry Data | [GEBCO](https://www.gebco.net/) | [Description](https://www.gebco.net/data-products/gridded-bathymetry-data) | [Download](https://www.gebco.net/data-products/gridded-bathymetry-data) | [Terms of use](https://www.gebco.net/data-products/gridded-bathymetry/terms-of-use) |
| International Best Track Archive for Climate Stewardship (**IBTrACS**) | [NOAA](https://www.ncei.noaa.gov/) [NCEI](https://www.ncei.noaa.gov/)| [Description](https://www.ncei.noaa.gov/products/international-best-track-archive) <br> [Download](https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r01/access/netcdf/) | [Citation](https://doi.org/10.25921/82ty-9e16) |
| **TPXO** Global Tidal Models | OSU | [Description](https://www.tpxo.net/global) <br> [TPXO Web Service](https://tpxows.azurewebsites.net/) | [Citation](https://journals.ametsoc.org/view/journals/atot/19/2/1520-0426_2002_019_0183_eimobo_2_0_co_2.xml) |
| **FES2022** (Finite Element Solution) - Global tide | [CLS, France](https://www.cls.fr/) | [Description](https://www.aviso.altimetry.fr/en/data/products/auxiliary-products/global-tide-fes.html) <br> [Abstract](https://ostst.aviso.altimetry.fr/programs/abstracts-details.html?tx_ausyclsseminar_pi2[action]=show&tx_ausyclsseminar_pi2[controller]=Abstracte&tx_ausyclsseminar_pi2[objAbstracte]=3287&cHash=X) |
| [国家地球系统科学数据中心](https://www.geodata.cn/main/) ([English version](http://wdcrre.data.ac.cn/)) | - | - |
| Monthly Climate/Ocean Indices (Time-Series) | [NOAA/PSL](https://psl.noaa.gov/) | [Website](https://psl.noaa.gov/data/timeseries/month/) <br> Including **`ENSO Indices`**, **`Non-ENSO`**, **`Atmosphere Teleconnections`** and so on |
| [NOAA/PSL data](https://psl.noaa.gov/data/timeseries/month/) | - | - |

<br>

## 🔧 常用工具:

| 工具名称 | 相关信息 |
| -------- | -------- |
| **Tide Prediction Tools** | **`pyTMD` (Python)** [Document](https://pytmd.readthedocs.io/en/latest/) &#124; [GitHub](https://github.com/pyTMD/pyTMD) &#124; [Citation](https://joss.theoj.org/papers/10.21105/joss.08566) &#124; <br> **`TMD` (MATLAB)** [Website(v3.0)](https://ww2.mathworks.cn/matlabcentral/fileexchange/133417-tide-model-driver-tmd-version-3-0) &#124; [GitHub(v3.0)](https://github.com/chadagreene/Tide-Model-Driver) &#124; [Citation(v3.0)](https://joss.theoj.org/papers/10.21105/joss.06018) <br> **`TMD` (MATLAB)** [Website(v2.5)](https://ww2.mathworks.cn/matlabcentral/fileexchange/75599-tide-model-driver-tmd-version-2-5-toolbox-for-matlab) &#124; [GitHub(v2.5)](https://github.com/EarthAndSpaceResearch/TMD_Matlab_Toolbox_v2.5) <br> **`OTPS` (FORTRAN)** [Website](https://www.tpxo.net/otps) |
| [earth.nullschool.net](https://earth.nullschool.net/) <br> An interactive website to visualize the motion of ocean and atmosphere | [Website](https://earth.nullschool.net/) <br> [Author: Cameron Beccario](https://github.com/cambecc) <br> [Nullschool Technologies Inc.](https://nullschool.net/)
| [**netCDF Operators (NCO)**](https://nco.sourceforge.net/) <br> A set of powerful netCDF-processing command-line programs | [Website](https://nco.sourceforge.net/) <br> [User Guide](https://nco.sourceforge.net/nco.html#NCO-User-Guide) <br> [GitHub](https://github.com/nco/nco) |
| [Thermodynamic Equation Of Seawater - 2010 (**TEOS-10**)](https://www.teos-10.org/) <br> A toolbox for calculating the thermodynamic properties of seawater | [Website](https://www.teos-10.org/) <br> [Software (GSW & SIA)](https://www.teos-10.org/software.htm) (supporting `MATLAB`, `Python`, `FORTRAN`...) <br> [Contents](https://www.teos-10.org/pubs/gsw/html/gsw_contents.html) | 
| Generic Mapping Tools (**GMT**) | [GMT developer](https://docs.gmt-china.org/latest/intro/) | [Website](https://www.generic-mapping-tools.org/) <br> [Doc](https://docs.gmt-china.org/latest/) <br> [GitHub](https://github.com/GenericMappingTools/gmt) |

<br>

## 🌐 数值模式

| 模式名称 | 机构 | 相关信息 |
| -------- | ---- | -------- |
| Regional Ocean Modeling System (**ROMS**) | The ROMS Group | [Website](https://www.myroms.org) <br> [GitHub](https://github.com/myroms/roms)
| Weather Research & Forecasting Model (**WRF**) | [NCAR](https://ncar.ucar.edu/) <br> [NOAA](https://www.noaa.gov/) <br> [U.S. Air Force](https://www.af.mil/) <br> [NRL](https://www.nrl.navy.mil/) <br> [OU](https://www.ou.edu/) <br> [FAA](https://www.faa.gov/) | [Website](https://www.mmm.ucar.edu/models/wrf) <br> [GitHub](https://github.com/wrf-model/WRF) <br> [Online Tutorial](https://www2.mmm.ucar.edu/wrf/OnLineTutorial/) |
| Princeton Ocean Model (**POM**) | [Princeton University](https://www.princeton.edu/) | [Website](https://www.pomusers.org) <br> [Wiki](https://en.wikipedia.org/wiki/Princeton_Ocean_Model) |
| Finite Volume Community Ocean Model (**FVCOM**) | [UMASS-D](https://www.umassd.edu/) <br> [WHOI](https://www.whoi.edu/) | [Website](https://www.fvcom.org/?p=5) <br> [GitHub](https://github.com/FVCOM-GitHub/FVCOM) |
| Modular Ocean Model (**MOM**) | [NOAA/GFDL](https://www.gfdl.noaa.gov/) | [Website](https://www.gfdl.noaa.gov/mom-ocean-model/) <br> [GitHub](https://github.com/NOAA-GFDL/MOM6-examples) |
| Nucleus for European Modelling of the Ocean (**NEMO**) | [NEMO Consortium](https://www.nemo-ocean.eu/consortium/history/) | [Website](http://www.nemo-ocean.eu/) <br> [Release](https://forge.nemo-ocean.eu/nemo/nemo/-/releases) |
| MIT General Circulation Model (**MITgcm**) | [MIT](https://web.mit.edu/) | [Website](http://mitgcm.org/) <br> [GitHub](https://github.com/MITgcm/MITgcm) <br> [Doc](https://mitgcm.readthedocs.io/en/latest/) |
| Parallel Ocean Program (**POP**) <br> (part of `CESM`) | [LANL](https://www.lanl.gov/) <br> [NCAR](https://ncar.ucar.edu/)| [Website](https://www.cesm.ucar.edu/models/pop)|
| Hybrid Coordinate Ocean Model (**HYCOM**) | [HYCOM Consortium](https://www.hycom.org/) | [Website](https://www.hycom.org/) <br> [GitHub](https://github.com/HYCOM) |
| Simulating WAves Nearshore (**SWAN**) | [TUDelft](https://www.tudelft.nl/en/) | [Website](https://swanmodel.sourceforge.io/) <br> [Reslease](https://swanmodel.sourceforge.io/download/download.htm) <br> [GitLab](https://gitlab.tudelft.nl/citg/wavemodels/swan) |
| **WAVEWATCH III** (WW3) | [NCEP](https://www.weather.gov/ncep/) | [GitHub](https://github.com/NOAA-EMC/WW3) |
| PALM | [PALM Group](https://www.meteo.uni-hannover.de/en/research/boundary-layer-meteorology) | [Website](https://palm.muk.uni-hannover.de/trac) <br> [Doc](https://docs.palm-model.com/) |
| Coupled Ocean–Atmosphere–Wave–Sediment Transport Modeling System (**COAWST**) <br> (include `ROMS`, `WRF`, `WRF_Hydro`, `SWAN`, `WAVEWATCHIII`, `InWave`, `sediment component`, and `sea ice model`) | [USGS](https://www.usgs.gov/) | [Website](https://www.usgs.gov/centers/whcmsc/science/coawst-a-coupled-ocean-atmosphere-wave-sediment-transport-modeling-system) <br> [GitHub](https://github.com/DOI-USGS/COAWST) |
| Community Earth System Model (**CESM**) <br> (include `CAM`, `CLM`, `CISM`) | [CGD](https://www.cgd.ucar.edu/) <br> [NCAR](https://ncar.ucar.edu/) | [Website](https://www.cesm.ucar.edu/) <br> [Release](https://www.cesm.ucar.edu/models) <br> [GitHub](https://github.com/ESCOMP/CESM) |
| Mass Conservation Ocean Model (MaCOM 妈祖) | [NMEFC](https://www.nmefc.cn/english) | [Website](https://macom.oceanguide.org.cn/) <br> [MaCOM](https://macom.oceanguide.org.cn/explain/circumflux/) <br> [FVWAM](https://macom.oceanguide.org.cn/explain/wave/) |
| LASG/IAP Climate Ocean Model (**LICOM**) | [IAP](https://iap.cas.cn/) | - |

<br>

## 🤖 海洋气象大模型

### 🌊 海洋大模型 (按发布时间排序)

| 大模型名称 | 机构 | 首次发布于 | 相关信息 |
| ---------- | ---- | ---------- | -------- |
| AI-GOMS 全球海洋建模系统 | [THU](https://www.dess.tsinghua.edu.cn/index.htm) | Aug 6, 2023 | [Arxiv](https://arxiv.org/abs/2308.03152) |
| “沧渊” OceanGPT | [ZJU](https://www.zju.edu.cn/) / [HIC](https://hic.zju.edu.cn/2024/0705/c85847a3039718/page.htm) | Oct 4, 2023 | [Website](https://zjunlp.github.io/project/OceanGPT/) <br> [Arxiv](https://arxiv.org/abs/2310.02031) <br> [GitHub](https://github.com/OceanGPT/OceanGPT) |
| “问海”海洋环境预报大模型 | [LSNL](https://www.lsnl.cn/) | May 27, 2024 | [Report](https://web.archive.org/web/20240605200610/https://news.ustc.edu.cn/info/1055/87684.htm) <br> [Nature Communications](https://doi.org/10.1038/s41467-025-57389-2) <br> [GitHub](https://github.com/Cuiyingzhe/WenHai) |
| “瀚海星云”科学人工智能基础大模型 | [LSNL](https://www.lsnl.cn/) | May 27, 2024 | [Report](https://web.archive.org/web/20240605200610/https://news.ustc.edu.cn/info/1055/87684.htm) |
| 璞云 (Puyun) | [metac-inc](https://www.metac-inc.com/) | Sep 1, 2024 | [Website](https://puyun.metac-inc.com/) <br> [Arxiv](https://arxiv.org/abs/2409.02123) <br> [GitHub](https://github.com/Yu-Kai-dev/ai-models-puyun) |
| “羲和”海洋环境预报大模型 (XiHe) | [NUDT](https://www.nudt.edu.cn/) | Oct 22, 2024 | [Arxiv](https://arxiv.org/abs/2402.02995) <br> [GitHub](https://github.com/Ocean-Intelligent-Forecasting/XiHe-GlobalOceanForecasting) |
| “波塞冬”海洋生态环境预报大模型 | [GS.ZJU](http://gs.zju.edu.cn/main.htm) | Nov, 2024 | [Report](http://gs.zju.edu.cn/2024/1128/c34773a2997394/page.htm) |
| “琅琊”海洋大模型 | [IOCAS](https://qdio.cas.cn/) | Dec 28, 2024 | [Report](https://www.cas.cn/cm/202501/t20250102_5044003.shtml) <br>  [Arxiv](https://doi.org/10.48550/arXiv.2412.18097)  <br> [GitHub](https://github.com/iocaswolfteam/LangYa_v1_0) |
| “瑶华”珊瑚礁多模态大模型 | [SCSIO](https://scsio.cas.cn/) | Mar, 2025 | [Report](https://web.archive.org/web/20250402154635/https://scsio.cas.cn/news/kydt/202503/t20250321_7563212.html) |
| “瀚海智语（OceanDS）”海洋大语言模型 | [NMEFC](https://www.nmefc.cn/) | Mar 31, 2025 | [Report](https://web.archive.org/web/20250401011835/https://paper.people.com.cn/rmrb/pc/content/202503/27/content_30064473.html) |
| “深蓝生命”大模型 | [OUC](https://www.ouc.edu.cn/main.htm) | Sep, 2025 | [Report](https://m.chinanews.com/wap/detail/chs/zw/396326.shtml) |
| “海冰”大模型 | [OUC](https://www.ouc.edu.cn/main.htm) | Sep, 2025 | [Report](https://m.chinanews.com/wap/detail/chs/zw/396326.shtml) |
| 深海生境智能认知与探索多模态大模型(DePTH-GPT) | [SIO](https://www.sio.org.cn/) / [Zhejiang Lab](https://www.zhejianglab.org/lab/home) | Nov 6, 2025 | [Report](https://www.sio.org.cn/a/snyw/22983.html) |
| NAUTILUS 水下多模态大模型 | [HUST](https://www.hust.edu.cn/) | Oct 31, 2025 | [Website](https://h-embodvis.github.io/NAUTILUS/) <br> [Arxiv](https://arxiv.org/abs/2510.27481) <br> [GitHub](https://github.com/H-EmbodVis/NAUTILUS) |
| 黑潮智能预报系统KIPS | [HHU](https://www.hhu.edu.cn/) | Mar 11, 2025 | [Report](https://kuroshio-prediction.net/article.html?id=9) <br> [Website](https://kuroshio-prediction.net/) |
| TritonCast |  [THU](https://www.dess.tsinghua.edu.cn/index.htm) | May 26, 2025 | [Arxiv](https://www.dess.tsinghua.edu.cn/index.htm)  | 
| “瞰海”全链路海洋AI大模型 | [SAI.SYSU](https://sai.sysu.edu.cn/) / [NSOAS](http://www.nsoas.org.cn/index.html) | Nov 24, 2025 | [Report](https://www.ncsti.gov.cn/kjdt/kjrd/202511/t20251126_230096.html) <br> [GitHub](https://github.com/skyocean-kanhai/KanHai) |
| 海境·区域海洋环境应用大模型1.0 <br> （界面大模型、区域预报大模型、涡流大模型、智能问答大模型） | [SCSIO](http://sklto.scsio.ac.cn/) | Jan, 2026 | [Report](https://mp.weixin.qq.com/s/kzLxA482HqWAxi6O1iZQzg) |


### 🌦️ 气象大模型 (按发布时间排序)

| 大模型名称 | 机构 | 首次发布于 | 相关信息 |
| ---------- | ---- | ---------- | -------- |
| MetNet | [Google Research](https://research.google/) | Mar 24, 2020 | [Website](https://research.google/blog/metnet-3-a-state-of-the-art-neural-weather-model-available-in-google-products/) <br> [Arxiv](https://doi.org/10.48550/arXiv.2003.12140) <br> [GitHub](https://github.com/lucidrains/metnet3-pytorch) |
| FourCastNet | [NVIDIA](https://www.nvidia.com/en-sg/) | Feb 22, 2022 | [Arxiv](https://arxiv.org/abs/2202.11214) <br> [GitHub](https://github.com/NVlabs/FourCastNet) |
| 书生·风乌 气象海洋预报大模型体系 | [ShLab](https://www.shlab.org.cn/) | Apr 7, 2023 | [Website](https://fengwu.intern-ai.org.cn/) <br> [Arxiv](https://arxiv.org/abs/2304.02948) |
| “伏羲”大模型 FUXI | [FDU](https://www.fudan.edu.cn/main.htm) | Jun 22, 2023 | [Website](https://fuxi-ai.cn/) <br> [Nature](https://www.nature.com/articles/s41612-023-00512-1) <br> [Arxiv](https://arxiv.org/abs/2306.12873) <br> [GitHub](https://github.com/tpys/FuXi) |
| “盘古”大模型 Pangu | [Huawei Cloud](https://www.huaweicloud.com/intl/en-us/) | Jul 5, 2023 | [Website](https://www.huaweicloud.com/product/pangu.html) <br> [Nature](https://www.nature.com/articles/s41586-023-06185-3) |
| GraphCast | [Google DeepMind](https://deepmind.google/) | Nov 14, 2023 | [Science](https://www.science.org/doi/10.1126/science.adi2336) <br> [GitHub](https://github.com/google-deepmind/graphcast) |
| “风清”“风雷”“风顺” | [CMA](https://www.cma.gov.cn/) / [THU](https://www.tsinghua.edu.cn/) | Jun 18, 2024 | [Report](https://www.tsinghua.edu.cn/info/1182/112354.htm) |
| NeuralGCM | [Google Research](https://research.google/) | Jul 22, 2024 | [Science](https://www.science.org/doi/10.1126/science.adi2336) <br> [GitHub](https://github.com/neuralgcm/neuralgcm) |
| “演天”气象预报大模型 | [IAP](https://iap.cas.cn/) | Oct 17, 2024 | [Report](https://iap.cas.cn/gb/xwdt/zhxw/202410/t20241017_7402105.html) <br> [Arxiv](https://arxiv.org/abs/2410.04539) |
| Aardvark Weather | [Cantab](https://www.cst.cam.ac.uk/) | Mar 20, 2025 | [Nature](https://doi.org/10.1038/s41586-025-08897-0) <br> [GitHub](https://github.com/anna-allen/aardvark-weather-public) |

<br>

## 🤝 如何贡献
我们欢迎大家提供信息，帮助我们维持这份列表的准确性并不断完善！

- 您可以直接提交Pull & Request来添加新的数据集或更新现有数据集。
- 此外，如果您发现任何失效链接、过时信息，或对要添加的新数据集有任何建议，
都可以提出issue。

<br>

## 📜 开源许可
此代码库采用 MIT 许可证授权。详情请参阅 [LICENSE](LICENSE) 文件。

<br>

## 📥 未来计划

我们计划在未来扩展此列表，以涵盖更多领域的数据集，例如:

<details>
<summary>遥感数据</summary>

- MODIS (Terra & Aqua)
- TOPEX/Poseidon
- CMEMS Altimetry Products
- QuikSCAT
- SeaWiFS
- SWOT
- ...... 
</details>

<details>
<summary>再分析数据</summary>

- NCEP/NCAR Reanalysis
- ORAS5
- ...... 
</details>

<details>
<summary>预报数据</summary>

- GFS (Global Forecast System)
- HYCOM
- CMEMS Global Ocean Forecast
- ...... 
</details>

<details>
<summary>现场观测</summary>

- TAO/TRITON / PIRATA / RAMA (for ENSO)
- ...... 
</details>
