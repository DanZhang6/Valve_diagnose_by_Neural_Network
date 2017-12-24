k=1;
for i=1:5629
    if Dev_X(281,i)~=1
        Anomaly(:,k)=Dev_X(:,i);
        k=k+1;
    end
end