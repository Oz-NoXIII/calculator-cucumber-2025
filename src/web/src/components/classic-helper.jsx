export default function ClassicHelper() {
  return (
    <div className="py-1.5 px-4 h-full flex flex-col justify-between">
      <div className="grid gap-3 grid-cols-2">
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">Infix</p>
          <div className="grid pl-4 text-sm">
            <p>
              <span className="font-bold">Addition :</span> a + b
            </p>
            <p>
              <span className="font-bold">Subtraction :</span> a - b
            </p>
            <p>
              <span className="font-bold">Multiplication :</span> a * b
            </p>
            <p>
              <span className="font-bold">Division :</span> a / b
            </p>
            <p>
              <span className="font-bold">Exponentiation :</span> a ^ b
            </p>
            <p>
              <span className="font-bold">Negation :</span> (-a)
            </p>
            <p>
              <span className="font-bold">Inverse :</span> inv(a)
            </p>
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">Prefix</p>
          <div className="grid pl-4 text-sm">
            <p>
              <span className="font-bold">Addition :</span> +(a, b){' '}
              <span className="text-muted-foreground/60 font-medium text-xs">
                or
              </span>{' '}
              +(a b)
            </p>
            <p>
              <span className="font-bold">Subtraction :</span> -(a, b){' '}
              <span className="text-muted-foreground/60 font-medium text-xs">
                or
              </span>{' '}
              -(a b)
            </p>
            <p>
              <span className="font-bold">Multiplication :</span> *(a, b){' '}
              <span className="text-muted-foreground/60 font-medium text-xs">
                or
              </span>{' '}
              *(a b)
            </p>
            <p>
              <span className="font-bold">Division :</span> /(a, b){' '}
              <span className="text-muted-foreground/60 font-medium text-xs">
                or
              </span>{' '}
              /(a b)
            </p>
            <p>
              <span className="font-bold">Exponentiation :</span> ^(a, b){' '}
              <span className="text-muted-foreground/60 font-medium text-xs">
                or
              </span>{' '}
              ^(a b)
            </p>
            <p>
              <span className="font-bold">Negation :</span> (-(a))
            </p>
            <p>
              <span className="font-bold">Inverse :</span> inv(a)
            </p>
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">Postfix</p>
          <div className="grid pl-4 text-sm">
            <p>
              <span className="font-bold">Addition :</span> (a, b)+{' '}
              <span className="text-muted-foreground/60 font-medium text-xs">
                or
              </span>{' '}
              (a b)+
            </p>
            <p>
              <span className="font-bold">Subtraction :</span> (a, b)-{' '}
              <span className="text-muted-foreground/60 font-medium text-xs">
                or
              </span>{' '}
              (a b)-
            </p>
            <p>
              <span className="font-bold">Multiplication :</span> (a, b)*{' '}
              <span className="text-muted-foreground/60 font-medium text-xs">
                or
              </span>{' '}
              (a b)*
            </p>
            <p>
              <span className="font-bold">Division :</span> (a, b)/{' '}
              <span className="text-muted-foreground/60 font-medium text-xs">
                or
              </span>{' '}
              (a b)/
            </p>
            <p>
              <span className="font-bold">Exponentiation :</span> (a, b)^{' '}
              <span className="text-muted-foreground/60 font-medium text-xs">
                or
              </span>{' '}
              (a b)^
            </p>
            <p>
              <span className="font-bold">Negation :</span> (a-)-
            </p>
            <p>
              <span className="font-bold">Inverse :</span> inv(a)
            </p>
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">Others</p>
          <div className="grid pl-4 text-sm">
            <p>
              <span className="font-bold">Multiple operands :</span> +(a, b, c)
            </p>
            <p>
              <span className="font-bold">Nested operations :</span> *(a, +(b,
              c))
            </p>
            <p>
              <span className="font-bold">Parentheses :</span> (a + b) * c
            </p>
            <p>
              <span className="font-bold">Integers :</span> 7
            </p>
            <p>
              <span className="font-bold">Rational numbers :</span> 0.245
            </p>
            <p>
              <span className="font-bold">Complex numbers :</span> a + bj
            </p>
          </div>
        </div>
      </div>
      <div className="flex flex-col col-span-2 gap-3">
        <p className="text-muted-foreground text-xs">Notes</p>
        <p className="text-sm text-orange-600">
          The result type matches the input : integers yield integers, rationals
          yield rationals, and complex inputs yield complex results.
        </p>
      </div>
    </div>
  );
}
