setwd('~/Documents/Carbon data mission/')
a <- read.csv('C02_emissions.csv',skip=1,header=TRUE,na.strings=c('--',' ','NA'))
names(a) <- scan("C02_emissions.csv", what = character(), nlines=1,sep =',')

head(a)

# ind <- a$Country=="Japan"
# india <- a[ind,]
# plot(1980:2009,as.vector(as.matrix(india[6:35])),ylim=c(0,8000))

# fits <- list()
# for (i in a$Country){
#   ind <- a$Country== i
#   india <- a[ind,]
#   values <- as.numeric(as.vector(as.matrix(india[6:35])))
#   b <- lines(1980:2009,values)
# #  fits[[i]] <- b$coefficients
#   }


#c <- na.omit(a)
## only remove NA in column 1: Emissions rank in 2009 ## 
c <- a[complete.cases(a[,1]),]
countryLabels <- list()

for (i in seq_along((c$Country))){
  if (c[i,1] <= 5){
    india <- c[i,]
    values <- as.numeric(as.vector(as.matrix(india[6:35])))
    max_ind <- which.max(values)
    values <- values#/values[max_ind]
    append(countryLabels, c$Country[i],length(countryLabels))
    
    if (i == 1){
      plot(1980:2009,values,"l")
    }
    
    if (i > 1){
      par(new=T)
      plot(1980:2009,values,"l",axes=F)      
    }
  }  
}

legend(1983,7000,countryLabels)

#legend(2000,9.5, c("Health","Defense"), lty=c(1,1),lwd=c(2.5,2.5),col=c("blue","red")) 

