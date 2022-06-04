% Measure the PA slope for 1226062160_psr2.cut2.ar.drm

% Load the data from the pdv output file.
% We recognise by inspection of the profile that the six PA points of interest
% occupy phase bins 78 through 83 (which is rows 79 through 84).
dat = load("1226062160_psr2.cut2.ar.drm.pdv")(79:84,:);
nbins = 128;

% Extracting out the relevant data:
ph    = dat(:,3)*360/nbins; % The phase, in degrees
PA    = dat(:,8);           % The PA, in degrees
PAerr = dat(:,9);           % The error in PA, in degrees

% Set up the problem as a weighted least squares
Y = PA;
W = diag(1./PAerr.^2);
X = [ones(size(ph)), ph];

% And apply the formula
b = pinv(X'*W*X)*(X'*W*Y);

% The slope (in deg/deg) will be the second element of "b"
slope = b(2);

% Print it out nicely
printf( "%.1f°/°\n", slope );
