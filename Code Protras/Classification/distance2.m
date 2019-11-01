function [D]=distance2(X,Y,A)
% computes sq. A-norm distance between two D-dimensional vectors

if(nargin<3)
    A=eye(size(X,2));
end
%disp([sum(Y*A.*Y,2)]');
V = bsxfun(@plus,-2*X*A*Y',sum(X*A.*X,2));
F = [sum(Y*A.*Y,2)]';
temp = bsxfun(@plus,bsxfun(@plus,-2*X*A*Y',sum(X*A.*X,2)),[sum(Y*A.*Y,2)]');
D=sqrt(bsxfun(@plus,bsxfun(@plus,-2*X*A*Y',sum(X*A.*X,2)),[sum(Y*A.*Y,2)]'));
disp(D);
G = bsxfun(@plus,bsxfun(@plus,-2*X*A*Y',sum(X*A.*X,2)),[sum(Y*A.*Y,2)]');
disp(sum(D,1));
disp('Ay yo');