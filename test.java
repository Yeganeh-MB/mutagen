class Test {
    public void main(String[] args) {
        int a = 3, s=10,
            b = 10;

        int[] arr = new int[3];
        arr[0] = 1;

        double c = a + 3;

        SomeClass test = new SomeClass(a);

        a.InnerClass b = new a.InnerClass( test );

        for (int i=0; i<3; i+=1) {
            b %=1;
        }

        if (((a)<(b+3)&&c>a) || (a++ > !b)) {
            System.console.out( a.somemethod("here is something!") );
            b--;
        }

        return a;
    }
}