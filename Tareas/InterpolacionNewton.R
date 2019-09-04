newtoninter(x, y, p) <- function (f, a, d) 
n = length(x);
d(:,1)=y';
for j=2:n
for i=j:n
d(i,j)= ( d(i-1,j-1)-d(i,j-1)) / (x(i-j+1)-x(i));
end
end
a = diag(d)';

Df(1,:) = repmat(1, size(p));
c(1,:) = repmat(a(1), size(p));
for j = 2 : n
Df(j,:)=(p - x(j-1)) .* Df(j-1,:);
c(j,:) = a(j) .* Df(j,:);
end
f=sum(c);

Chebyshev <- function()

a = -6; b = 6;
n = 15;
x = cos( (2 * (1:n) - 1) / (2 * n) * pi);



# (2) f(x) = 1 / (1 + 25 * x^2)
y = 1 / (1 + 25 * x^2);
truth = 1 / (1 + 25 * p^2);
f= newtoninter(x,y,p);


plot(x,y,'ob', col = "blue", xlim = c(-0.5,0.5));
plot(p,truth,'-b');
plot(p,f,'-r');
title('Newton Interpolation: Chebyshev nodes');
legend('samples', 'truth', 'interpolation');
end(Chebyshev)
