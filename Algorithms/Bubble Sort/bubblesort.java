public class array {
	static Scanner scn = new Scanner(System.in);

	public static void main(String[] args) {
        int[] arr2 = takeinput();
        bubblesort(arr2);
        display(arr2);
    }
    public static int[] takeinput() {
		int n = scn.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i <= arr.length - 1; i++) {
			arr[i] = scn.nextInt();
		}
		return arr;
	}

	public static void display(int[] arr) {
		for (int i = 0; i <= arr.length - 1; i++) {
			System.out.println(arr[i]);
		}
	}
public static void bubblesort(int[] arr) {
    for (int c = 0; c < arr.length - 1; c++) {
        for (int j = 0; j < arr.length - 1 - c; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}