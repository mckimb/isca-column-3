netcdf mlw.t{                                                                   

dimensions:
    lat            =   1;
    lon            =   1;
    plev           = 122;


variables:
    float lat(lat);                                                           
             lat:units = "degree";                                            
             lat:title = "LATITUDE";                                         
    float lon(lon);                                                           
             lon:units = "degree";                                            
             lon:title = "LONGITUDE";                                        
    float plev(plev);                                                         
             plev:units = "Pa";                                               
             plev:title = "PRESSURE";                                        

    float t(plev,lon,lat);                                                     
             t:units = "K";                                                   
             t:title = "TEMPERATURE";                                                        

data:                                                                           
              lat =   .000000E+00;
              lon =   .000000E+00;
             plev =   .500000E-01,  .108300E+00,  .126260E+00,  .147210E+00,
                      .171640E+00,  .200110E+00,  .233320E+00,  .272030E+00,
                      .317160E+00,  .369780E+00,  .431130E+00,  .502660E+00,
                      .586060E+00,  .683300E+00,  .796670E+00,  .928850E+00,
                      .108300E+01,  .126260E+01,  .147210E+01,  .171640E+01,
                      .200110E+01,  .233320E+01,  .272030E+01,  .317160E+01,
                      .369780E+01,  .431130E+01,  .502660E+01,  .586060E+01,
                      .683300E+01,  .796670E+01,  .928850E+01,  .108300E+02,
                      .126260E+02,  .147210E+02,  .171640E+02,  .200110E+02,
                      .233320E+02,  .272030E+02,  .317160E+02,  .369780E+02,
                      .431130E+02,  .502660E+02,  .586060E+02,  .683300E+02,
                      .796670E+02,  .928850E+02,  .108300E+03,  .126260E+03,
                      .147210E+03,  .171640E+03,  .200110E+03,  .233320E+03,
                      .272030E+03,  .317160E+03,  .369780E+03,  .431130E+03,
                      .502660E+03,  .586060E+03,  .683300E+03,  .796670E+03,
                      .928850E+03,  .108300E+04,  .126260E+04,  .147210E+04,
                      .171640E+04,  .200110E+04,  .233320E+04,  .272030E+04,
                      .317160E+04,  .369780E+04,  .431130E+04,  .502660E+04,
                      .586060E+04,  .683300E+04,  .796670E+04,  .928850E+04,
                      .110000E+05,  .130000E+05,  .150000E+05,  .170000E+05,
                      .190000E+05,  .210000E+05,  .230000E+05,  .250000E+05,
                      .270000E+05,  .290000E+05,  .310000E+05,  .330000E+05,
                      .350000E+05,  .370000E+05,  .390000E+05,  .410000E+05,
                      .430000E+05,  .450000E+05,  .470000E+05,  .490000E+05,
                      .510000E+05,  .530000E+05,  .550000E+05,  .570000E+05,
                      .590000E+05,  .610000E+05,  .630000E+05,  .650000E+05,
                      .670000E+05,  .690000E+05,  .710000E+05,  .730000E+05,
                      .750000E+05,  .770000E+05,  .790000E+05,  .810000E+05,
                      .830000E+05,  .850000E+05,  .870000E+05,  .890000E+05,
                      .910000E+05,  .930000E+05,  .950000E+05,  .970000E+05,
                      .990000E+05,  .100900E+06;
                t =   .212130E+03,  .212650E+03,  .213340E+03,  .214030E+03,
                      .214720E+03,  .215420E+03,  .216120E+03,  .216820E+03,
                      .217520E+03,  .218220E+03,  .218930E+03,  .219640E+03,
                      .220350E+03,  .221060E+03,  .221780E+03,  .222490E+03,
                      .223210E+03,  .223930E+03,  .224650E+03,  .225380E+03,
                      .226110E+03,  .226840E+03,  .227580E+03,  .228410E+03,
                      .229540E+03,  .231090E+03,  .232920E+03,  .234840E+03,
                      .236790E+03,  .238750E+03,  .240730E+03,  .242730E+03,
                      .244740E+03,  .246760E+03,  .248800E+03,  .250860E+03,
                      .252940E+03,  .255030E+03,  .257140E+03,  .259260E+03,
                      .261390E+03,  .263460E+03,  .264990E+03,  .265100E+03,
                      .263790E+03,  .261950E+03,  .259950E+03,  .257540E+03,
                      .254450E+03,  .250920E+03,  .247310E+03,  .243740E+03,
                      .240210E+03,  .236740E+03,  .233330E+03,  .229960E+03,
                      .226650E+03,  .223450E+03,  .220620E+03,  .218650E+03,
                      .217630E+03,  .217100E+03,  .216690E+03,  .216300E+03,
                      .215910E+03,  .215570E+03,  .215330E+03,  .215230E+03,
                      .215200E+03,  .215200E+03,  .215210E+03,  .215260E+03,
                      .215420E+03,  .215760E+03,  .216200E+03,  .216710E+03,
                      .217240E+03,  .217740E+03,  .218170E+03,  .218550E+03,
                      .218900E+03,  .219250E+03,  .219830E+03,  .221130E+03,
                      .223280E+03,  .225840E+03,  .228390E+03,  .230840E+03,
                      .233180E+03,  .235410E+03,  .237550E+03,  .239600E+03,
                      .241570E+03,  .243460E+03,  .245290E+03,  .247060E+03,
                      .248770E+03,  .250430E+03,  .252040E+03,  .253600E+03,
                      .255110E+03,  .256570E+03,  .257970E+03,  .259290E+03,
                      .260500E+03,  .261580E+03,  .262520E+03,  .263360E+03,
                      .264120E+03,  .264850E+03,  .265550E+03,  .266230E+03,
                      .266890E+03,  .267530E+03,  .268160E+03,  .268780E+03,
                      .269390E+03,  .269980E+03,  .270570E+03,  .271140E+03,
                      .271690E+03,  .272080E+03;

}                                                                               
