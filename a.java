public class a {
    public static void main(String[] args) {
        int a[]={0,1,0,3,12};
        int temp=0;

        for(int i=0;i<a.length;i++){

            for(int j=i+1;j<a.length;j++){
                if(a[i]>a[j]){
                    temp=a[i];
                    a[i]=a[j];
                    a[j]=temp;
                }
            }
        }
        for(int i=0;i<a.length;i++){ 
            int f = a[0],j;
            if(a[i]==0){
                for(j=0;j<a.length-1;j++){
                    a[j]=a[j+1];
                }
                a[j]=f;

            }
        }
        for(int i=0;i<a.length;i++){
            System.out.print(a[i]+" ");
        }
              
    }
}