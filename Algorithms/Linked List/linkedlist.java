package sept;

public class linkedlist {

	private class Node {
		int data;
		Node next;
	}

	private Node head;
	private Node tail;
	private int size;

	public void display() {
		Node temp = head;
		while (temp != null) {
			System.out.println(temp.data);
			temp = temp.next;
		}
	}

	public void addLast(int item) {
		Node nn = new Node();
		nn.data = item;
		nn.next = null;
		if (this.size >= 1) {
			this.tail.next = nn;
		}
		if (this.size == 0) {
			this.head = nn;
			this.tail = nn;
			this.size++;
		} else {
			this.tail = nn;
			this.size++;
		}
	}

	public void addFirst(int item) {
		Node nn = new Node();
		nn.data = item;
		nn.next = null;
		if (this.size >= 1) {
			nn.next = this.head;
		}
		if (this.size == 0) {
			this.head = nn;
			this.tail = nn;
			this.size++;
		} else {
			this.head = nn;
			this.size++;
		}
	}

	public int getFirst() throws Exception {
		if (this.size == 0) {
			throw new Exception("LL is empty");
		}
		return this.head.data;
	}

	public int getLast() throws Exception {
		if (this.size == 0) {
			throw new Exception("LL is empty");
		}
		return this.tail.data;
	}

	public int getAt(int idx) {
		Node temp = this.head;
		for (int j = 1; j <= idx; j++) {
			temp = temp.next;
		}
		return temp.data;
	}

	private Node getNodeAt(int idx) {
		Node temp = this.head;
		for (int j = 1; j <= idx; j++) {
			temp = temp.next;
		}
		return temp;
	}

	public void AddAt(int idx, int item) {
		if (idx == 0) {
			addFirst(item);
		}
		if (idx == this.size)
			addLast(item);

		Node nn = new Node();
		nn.data = item;
		nn.next = null;

		Node nm1 = getNodeAt(idx - 1);
		Node nm2 = getNodeAt(idx);
		nm1.next = nn;
		nn.next = nm2;

		this.size++;
	}

	public int removeFirst() {
		int rv = this.head.data;
		if (this.size == 1) {
			this.head = null;
			this.tail = null;
			this.size = 0;
		} else {
			this.head = this.head.next;
			this.size--;
		}
		return rv;
	}

	public int removeLast() {
		int rv = this.tail.data;
		if (this.size == 1) {
			this.head = null;
			this.tail = null;
			this.size = 0;
		} else {
			Node np2 = getNodeAt(this.size - 2);
			this.tail = np2;
			this.tail.next = null;
			this.size--;
		}
		return rv;
	}

	public void removeAt(int i) {
		if (i == 0) {
			removeFirst();
		} else if (i == this.size - 1) {
			removeLast();
		} else {
			Node n1 = getNodeAt(i - 1);
			Node n2 = getNodeAt(i);
			Node n3 = getNodeAt(i + 3);
			n1.next = n3;
			this.size--;
		}
	}

	public void reverse() {
		int l = 0;
		int r = this.size - 1;
		while (l < r) {
			Node n1 = getNodeAt(l);
			Node n2 = getNodeAt(r);
			int temp = n1.data;
			n1.data = n2.data;
			n2.data = temp;
			l++;
			r--;
		}
	}

	public void reversep() {
		Node prev = this.head;
		Node curr = prev.next;
		while (curr != null) {
			Node ahead = curr.next;
			curr.next = prev;
			prev = curr;
			curr = ahead;
		}
		Node t = this.head;
		this.head = this.tail;
		this.tail = t;
		this.tail.next = null;
	}

	public int mid() {
		Node slow = this.head;
		Node fast = this.head;
		while (fast.next != null && fast.next.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}
		return slow.data;
	}
}
