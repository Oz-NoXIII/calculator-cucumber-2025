export default function ScientificHelper() {
  return (
    <div className="py-1.5 px-4 h-full flex flex-col justify-between">
      <div className="grid gap-3 grid-cols-2">
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">Function</p>
          <div className="grid pl-4 text-sm">
            <p>
              <span className="font-bold">Sine function :</span> sin(a)
            </p>
            <p>
              <span className="font-bold">Cosine function :</span> cos(a)
            </p>
            <p>
              <span className="font-bold">Tangent function :</span> tan(a)
            </p>
            <p>
              <span className="font-bold">Inverse sine :</span> arcsin(a)
            </p>
            <p>
              <span className="font-bold">Inverse cosine :</span> arccos(a)
            </p>
            <p>
              <span className="font-bold">Inverse tangent :</span> arctan(a)
            </p>
            <p>
              <span className="font-bold">Hyperbolic sine :</span> sinh(a)
            </p>
            <p>
              <span className="font-bold">Hyperbolic cosine :</span> cosh(a)
            </p>
            <p>
              <span className="font-bold">Hyperbolic tangent :</span> tanh(a)
            </p>
            <p>
              <span className="font-bold">Logarithm base 10 :</span> log(a)
            </p>
            <p>
              <span className="font-bold">Natural logarithm :</span> ln(a)
            </p>
            <p>
              <span className="font-bold">N-th root :</span> a nroot b
            </p>
          </div>
        </div>
        <div className="flex flex-col gap-3">
          <p className="text-muted-foreground text-xs">Constants</p>
          <div className="grid pl-4 text-sm">
            <p>
              <span className="font-bold">Exponential :</span> e
            </p>
            <p>
              <span className="font-bold">Pi :</span> pi
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
