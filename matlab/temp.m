d=1/4; kd=2*pi*d;
i = 1:5;
psi = -2*kd*i/5;
zi = exp(i*psi);
a = fliplr(poly(zi));
a = steer(d, a, 0);
[g, ph] = array(d, a, 400);
dbz(ph, g, 45, 40);