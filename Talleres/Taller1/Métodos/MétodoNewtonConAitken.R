newtonAitken<-function(r,tol){
  i<-0
  error<-1
  while(i<=3 && error>tol){
    if(r!=0){ 
      bef=r
      r<-r-((Fx(r))/Dx(r))
      error<-(abs(bef-r))/abs(bef)
      cat("R=",r,"\t Error:",error,"i:",i,"\n")
      if(i==1)
      {
        x0=r
      }
      else
      {
        if(i==2)
        {
          x1=r
        } 
        else
        {
          x2=r
        }
      }
    }
    i=i+1
  }
  
  while(error>tol){
    if(r!=0){
      x3=x2-(((x2-x1)^2)/(x2-(2*x1)+x0))
      x0=x1
      x1=x2
      error<-(abs(x2-x3))/abs(x2)
      cat("R=",x3,"\t Error:",error,"i:",i,"\n")
      r<-r-((Fx(r))/Dx(r))
      x2=r
    }
    i=i+1
  }
}
