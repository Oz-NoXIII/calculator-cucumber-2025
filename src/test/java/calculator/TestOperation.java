package calculator;

//Import Junit5 libraries for unit testing:
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.*;
import visitor.Counter;

import java.util.Arrays;
import java.util.List;

class TestOperation {

	private Operation o;
	private Operation o2;

	@BeforeEach
	void setUp() throws Exception {
		List<Expression> params1 = Arrays.asList(new MyNumber(3), new MyNumber(4), new MyNumber(5));
		List<Expression> params2 = Arrays.asList(new MyNumber(5), new MyNumber(4));
		List<Expression> params3 = Arrays.asList(new Plus(params1), new Minus(params2), new MyNumber(7));
		o = new Divides(params3);
		o2 = new Divides(params3);
		o.accept(new Counter());
		o2.accept(new Counter());
	}

	@Test
	void testEquals() {
		assertEquals(o,o2);
	}

	@Test
	void testGetDepth() {
		assertEquals(2, o.getDepth());
	}

	@Test
	void testGetOps() {
		assertEquals(3, o.getOps());
	}

	@Test
	void testGetNbs() {
		assertEquals(Integer.valueOf(6), o.getNbs());
	}

}
