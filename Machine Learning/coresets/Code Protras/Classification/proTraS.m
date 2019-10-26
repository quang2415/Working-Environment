function [Ty,T,S] = proTraS(NT)
    [n, p] = size(NT);
    eps = 0.1;
    T = normalize(NT);
    s = 1; 
    x_init = get_init_point(T);
    [~, x_init_ind] = ismember(x_init, T, 'rows');
    Cost = 1;
    TI = (1:n)';
    Ty = zeros(n,1);
    S = x_init_ind;
    % contain group order number
    iS = [1];
    disp('ProTraS...');
    profile off
    profile on
    tic
    wr = [0];
    pre_max_dist = [0];
    weight = [0];
    idMax = [0];
    index_remove_group = [1];
    index_remove_elements =false(n,1);
    while Cost > eps
        index_remove_elements(S) = 1;
        diffPoints_Opt = TI(~index_remove_elements);
        Ty(S(end)) = s;
        %Tim khoang cach nho nhat cua mot diem den mot cum
        d = distance2(T(diffPoints_Opt,:), T(S(iS),:));
        [~, indMin] = min(d,[],2); %return index of S
        Ty(diffPoints_Opt) = iS(indMin);
        
        
        % bien Ty sau khi loai cac phan tu remove
        rTy = Ty;
        rTy(index_remove_elements) = [];
        
        sizeiS = size(iS,2);
        for yk = 1:sizeiS
            id = (rTy == iS(yk)); 
            [maxVal, idMaxTy] = max(d(id,yk)); 
            if isempty(maxVal)
                idMax(iS(yk)) = S(iS(yk));
                pre_max_dist(iS(yk)) = 0;
            else
                kk = diffPoints_Opt(id);
                idMax(iS(yk)) = kk(idMaxTy);
                pre_max_dist(iS(yk)) = maxVal;
            end
            weight(iS(yk)) =  numel(Ty(Ty ==iS(yk)));
        end
        
        wr = weight.*pre_max_dist;
        pk = wr/(max(weight)*max(pre_max_dist));
        [~,mInd] = max(pk);
        Cost = sum(wr)/n;
        S = [S; idMax(mInd)];  
        iS = 1:s;
        s = s + 1;
        % optimal
        % calculate yk to y*
        yk_xmax_dist = distance2(T(S(1:end-1),:),T(S(end),:));
        index_remove_group = yk_xmax_dist' > 2*pre_max_dist;
        iS = [iS(~index_remove_group) s];
        index_remove_group = find(index_remove_group == 1);
        index_remove_elements = ismember(Ty,index_remove_group);  
    end
    toc
    profile viewer    
    S(end) = [];    
    S = T(S,:);
end

