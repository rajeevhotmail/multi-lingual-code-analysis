# Go Project Analysis Report

Generated on: 2025-02-13 06:22:46

![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=flat&logo=go&logoColor=white)

## Contents
1. [Overview](#overview)
2. [Function Relationships](#function-relationships)
3. [Code Analysis](#code-analysis)

## Overview
Total files analyzed: 3

## Function Relationships

### File: `binding.go`

#### Function: `Language`
**Signature:** `func Language()`

**Documentation:**
```go
// Get the tree-sitter Language for this grammar.
```

**Operations:**
```go
Makes HTTP requests
```

<details>
<summary>Dependencies</summary>

- `unsafe.Pointer`
- `C.tree_sitter_python`

#### Called By:
- No incoming calls
</details>

### File: `value.go`

#### Function: `packEface`
**Signature:** `func packEface(v Value)`

**Documentation:**
```go
// packEface converts v to the empty interface.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `panic`
- `typedmemmove`
- `unsafe.Pointer`
- `unsafe_New`
- `ifaceIndir`
- `(*unsafe.Pointer)`
- `(*emptyInterface)`

#### Called By:
- No incoming calls
</details>

#### Function: `unpackEface`
**Signature:** `func unpackEface(i interface{})`

**Documentation:**
```go
// unpackEface converts the empty interface i to a Value.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `flag`
- `unsafe.Pointer`
- `t.Kind`
- `ifaceIndir`
- `(*emptyInterface)`

#### Called By:
- No incoming calls
</details>

#### Function: `methodName`
**Signature:** `func methodName()`

**Documentation:**
```go
// assumed to be two stack frames above.
```

**Operations:**
```go
Makes HTTP requests
```

<details>
<summary>Dependencies</summary>

- `runtime.FuncForPC`
- `runtime.Caller`
- `f.Name`

#### Called By:
- No incoming calls
</details>

#### Function: `callReflect`
**Signature:** `func callReflect(ctxt *makeFuncImpl, frame unsafe.Pointer)`

**Documentation:**
```go
// The gc compilers know to do that for the name "reflect.callReflect".
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `append`
- `flag`
- `f`
- `panic`
- `align`
- `typ.String`
- `typedmemmove`
- `typ.Kind`
- `len`
- `make`
- `uintptr`
- `unsafe.Pointer`
- `funcName`
- `unsafe_New`
- `ifaceIndir`
- `(*unsafe.Pointer)`
- `out[i].typ.String`

#### Called By:
- No incoming calls
</details>

#### Function: `methodReceiver`
**Signature:** `func methodReceiver(op string, v Value, methodIndex int)`

**Documentation:**
```go
// The return value fn is a pointer to the method code.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `uint`
- `panic`
- `v.typ.Kind`
- `len`
- `(*nonEmptyInterface)`
- `(*interfaceType)`
- `unsafe.Pointer`
- `v.typ.uncommon`

#### Called By:
- No incoming calls
</details>

#### Function: `storeRcvr`
**Signature:** `func storeRcvr(v Value, p unsafe.Pointer)`

**Documentation:**
```go
// methods, which always uses one word to record the receiver.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `ifaceIndir`
- `t.Kind`
- `(*unsafe.Pointer)`
- `(*nonEmptyInterface)`

#### Called By:
- No incoming calls
</details>

#### Function: `align`
**Signature:** `func align(x, n uintptr)`

**Documentation:**
```go
// n must be a power of two.
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `callMethod`
**Signature:** `func callMethod(ctxt *methodValue, frame unsafe.Pointer)`

**Documentation:**
```go
// The gc compilers know to do that for the name "reflect.callMethod".
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `methodReceiver`
- `typedmemmovepartial`
- `align`
- `framePool.Get`
- `storeRcvr`
- `uint32`
- `call`
- `funcLayout`
- `uintptr`
- `unsafe.Pointer`
- `memclr`
- `framePool.Put`

#### Called By:
- No incoming calls
</details>

#### Function: `funcName`
**Signature:** `func funcName(f func([]Value) []Value)`

**Documentation:**
```go
// funcName returns the name of f, for use in error messages.
```

**Operations:**
```go
Makes HTTP requests
```

<details>
<summary>Dependencies</summary>

- `unsafe.Pointer`
- `runtime.FuncForPC`
- `rf.Name`
- `(*uintptr)`

#### Called By:
- No incoming calls
</details>

#### Function: `valueInterface`
**Signature:** `func valueInterface(v Value, safe bool)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `panic`
- `packEface`
- `v.NumMethod`
- `makeMethodValue`
- `v.kind`

#### Called By:
- No incoming calls
</details>

#### Function: `overflowFloat32`
**Signature:** `func overflowFloat32(x float64)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Makes HTTP requests
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `typesMustMatch`
**Signature:** `func typesMustMatch(what string, t1, t2 Type)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `t2.String`
- `panic`
- `t1.String`

#### Called By:
- No incoming calls
</details>

#### Function: `arrayAt`
**Signature:** `func arrayAt(p unsafe.Pointer, i int, eltSize uintptr)`

**Documentation:**
```go
// eltSize wide (in bytes).
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `unsafe.Pointer`
- `uintptr`

#### Called By:
- No incoming calls
</details>

#### Function: `grow`
**Signature:** `func grow(s Value, extra int)`

**Documentation:**
```go
// more capacity if needed. It also returns the old and new slice lengths.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `MakeSlice`
- `panic`
- `Copy`
- `s.Slice`
- `s.Cap`
- `s.Len`
- `s.Type`

#### Called By:
- No incoming calls
</details>

#### Function: `Append`
**Signature:** `func Append(s Value, x ...Value)`

**Documentation:**
```go
// As in Go, each x's value must be assignable to the slice's element type.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `s.Index`
- `len`
- `grow`
- `s.mustBe`
- `s.Index(i).Set`

#### Called By:
- No incoming calls
</details>

#### Function: `AppendSlice`
**Signature:** `func AppendSlice(s, t Value)`

**Documentation:**
```go
// The slices s and t must have the same element type.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `t.Type().Elem`
- `typesMustMatch`
- `t.Type`
- `Copy`
- `s.Slice`
- `t.Len`
- `s.Type`
- `grow`
- `s.mustBe`
- `s.Type().Elem`
- `t.mustBe`

#### Called By:
- No incoming calls
</details>

#### Function: `Copy`
**Signature:** `func Copy(dst, src Value)`

**Documentation:**
```go
// dst and src must have the same element type.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `panic`
- `dst.typ.Elem`
- `src.Len`
- `typedslicecopy`
- `dst.mustBeExported`
- `dst.kind`
- `src.kind`
- `src.typ.Elem`
- `src.mustBeExported`
- `dst.mustBeAssignable`
- `dst.Len`
- `de.common`
- `(*sliceHeader)`
- `typesMustMatch`

#### Called By:
- No incoming calls
</details>

#### Function: `rselect`
**Signature:** `func rselect([]runtimeSelect)`

**Documentation:**
```go
//go:noescape
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `Select`
**Signature:** `func Select(cases []SelectCase)`

**Documentation:**
```go
// (as opposed to a zero value received because the channel is closed).
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `panic`
- `len`
- `ch.pointer`
- `unsafe.Pointer`
- `ChanDir`
- `v.IsValid`
- `ch.IsValid`
- `ch.mustBeExported`
- `c.Chan.IsValid`
- `(*chanType)`
- `unsafe_New`
- `v.mustBeExported`
- `v.assignTo`
- `make`
- `t.Kind`
- `c.Send.IsValid`
- `ifaceIndir`
- `flag`
- `ch.mustBe`
- `uintptr`
- `rselect`
- `(*unsafe.Pointer)`

#### Called By:
- No incoming calls
</details>

#### Function: `unsafe_New`
**Signature:** `func unsafe_New(*rtype)`

**Documentation:**
```go
// implemented in package runtime
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `unsafe_NewArray`
**Signature:** `func unsafe_NewArray(*rtype, int)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `MakeSlice`
**Signature:** `func MakeSlice(typ Type, len, cap int)`

**Documentation:**
```go
// for the specified slice type, length, and capacity.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `flag`
- `panic`
- `unsafe_NewArray`
- `typ.Kind`
- `typ.common`
- `typ.Elem`
- `unsafe.Pointer`

#### Called By:
- No incoming calls
</details>

#### Function: `MakeChan`
**Signature:** `func MakeChan(typ Type, buffer int)`

**Documentation:**
```go
// MakeChan creates a new channel with the specified type and buffer size.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `makechan`
- `flag`
- `panic`
- `typ.Kind`
- `typ.common`
- `uint64`
- `typ.ChanDir`

#### Called By:
- No incoming calls
</details>

#### Function: `MakeMap`
**Signature:** `func MakeMap(typ Type)`

**Documentation:**
```go
// MakeMap creates a new map of the specified type.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `flag`
- `panic`
- `typ.Kind`
- `typ.common`
- `makemap`

#### Called By:
- No incoming calls
</details>

#### Function: `Indirect`
**Signature:** `func Indirect(v Value)`

**Documentation:**
```go
// If v is not a pointer, Indirect returns v.
```

**Operations:**
```go
Makes HTTP requests
```

<details>
<summary>Dependencies</summary>

- `v.Kind`
- `v.Elem`

#### Called By:
- No incoming calls
</details>

#### Function: `ValueOf`
**Signature:** `func ValueOf(i interface{})`

**Documentation:**
```go
// stored in the interface i.  ValueOf(nil) returns the zero Value.
```

**Operations:**
```go
Performs unit testing and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `unpackEface`
- `escapes`

#### Called By:
- No incoming calls
</details>

#### Function: `Zero`
**Signature:** `func Zero(typ Type)`

**Documentation:**
```go
// The returned value is neither addressable nor settable.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `flag`
- `panic`
- `typ.common`
- `t.Kind`
- `unsafe_New`
- `ifaceIndir`

#### Called By:
- No incoming calls
</details>

#### Function: `New`
**Signature:** `func New(typ Type)`

**Documentation:**
```go
// for the specified type.  That is, the returned Value's Type is PtrTo(typ).
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `flag`
- `panic`
- `typ.common`
- `typ.common().ptrTo`
- `unsafe_New`

#### Called By:
- No incoming calls
</details>

#### Function: `NewAt`
**Signature:** `func NewAt(typ Type, p unsafe.Pointer)`

**Documentation:**
```go
// specified type, using p as that pointer.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `flag`
- `typ.common().ptrTo`
- `typ.common`

#### Called By:
- No incoming calls
</details>

#### Function: `convertOp`
**Signature:** `func convertOp(dst, src *rtype)`

**Documentation:**
```go
// to a value of type dst. If the conversion is illegal, convertOp returns nil.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `src.Kind`
- `src.Elem`
- `dst.Name`
- `dst.Elem`
- `implements`
- `src.Elem().Kind`
- `src.Elem().PkgPath`
- `haveIdenticalUnderlyingType`
- `src.Name`
- `dst.Elem().common`
- `dst.Kind`
- `dst.Elem().PkgPath`
- `src.Elem().common`
- `dst.Elem().Kind`

#### Called By:
- No incoming calls
</details>

#### Function: `makeInt`
**Signature:** `func makeInt(f flag, bits uint64, t Type)`

**Documentation:**
```go
// where t is a signed or unsigned int type.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `flag`
- `(*uint16)`
- `t.common`
- `uint16`
- `uint32`
- `typ.Kind`
- `(*uint8)`
- `unsafe.Pointer`
- `(*uint32)`
- `unsafe_New`
- `uint8`
- `(*uint64)`

#### Called By:
- No incoming calls
</details>

#### Function: `makeFloat`
**Signature:** `func makeFloat(f flag, v float64, t Type)`

**Documentation:**
```go
// where t is a float32 or float64 type.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `flag`
- `t.common`
- `float32`
- `typ.Kind`
- `unsafe.Pointer`
- `(*float32)`
- `unsafe_New`
- `(*float64)`

#### Called By:
- No incoming calls
</details>

#### Function: `makeComplex`
**Signature:** `func makeComplex(f flag, v complex128, t Type)`

**Documentation:**
```go
// where t is a complex64 or complex128 type.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `flag`
- `t.common`
- `(*complex64)`
- `(*complex128)`
- `typ.Kind`
- `unsafe.Pointer`
- `complex64`
- `unsafe_New`

#### Called By:
- No incoming calls
</details>

#### Function: `makeString`
**Signature:** `func makeString(f flag, v string, t Type)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `ret.SetString`
- `New`
- `New(t).Elem`

#### Called By:
- No incoming calls
</details>

#### Function: `makeBytes`
**Signature:** `func makeBytes(f flag, v []byte, t Type)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `New`
- `New(t).Elem`
- `ret.SetBytes`

#### Called By:
- No incoming calls
</details>

#### Function: `makeRunes`
**Signature:** `func makeRunes(f flag, v []rune, t Type)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `ret.setRunes`
- `New`
- `New(t).Elem`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtInt`
**Signature:** `func cvtInt(v Value, t Type)`

**Documentation:**
```go
// convertOp: intXX -> [u]intXX
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `v.Int`
- `uint64`
- `makeInt`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtUint`
**Signature:** `func cvtUint(v Value, t Type)`

**Documentation:**
```go
// convertOp: uintXX -> [u]intXX
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `v.Uint`
- `makeInt`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtFloatInt`
**Signature:** `func cvtFloatInt(v Value, t Type)`

**Documentation:**
```go
// convertOp: floatXX -> intXX
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `int64`
- `v.Float`
- `uint64`
- `makeInt`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtFloatUint`
**Signature:** `func cvtFloatUint(v Value, t Type)`

**Documentation:**
```go
// convertOp: floatXX -> uintXX
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `v.Float`
- `uint64`
- `makeInt`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtIntFloat`
**Signature:** `func cvtIntFloat(v Value, t Type)`

**Documentation:**
```go
// convertOp: intXX -> floatXX
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `float64`
- `makeFloat`
- `v.Int`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtUintFloat`
**Signature:** `func cvtUintFloat(v Value, t Type)`

**Documentation:**
```go
// convertOp: uintXX -> floatXX
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `float64`
- `makeFloat`
- `v.Uint`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtFloat`
**Signature:** `func cvtFloat(v Value, t Type)`

**Documentation:**
```go
// convertOp: floatXX -> floatXX
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `makeFloat`
- `v.Float`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtComplex`
**Signature:** `func cvtComplex(v Value, t Type)`

**Documentation:**
```go
// convertOp: complexXX -> complexXX
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `makeComplex`
- `v.Complex`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtIntString`
**Signature:** `func cvtIntString(v Value, t Type)`

**Documentation:**
```go
// convertOp: intXX -> string
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `makeString`
- `v.Int`
- `string`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtUintString`
**Signature:** `func cvtUintString(v Value, t Type)`

**Documentation:**
```go
// convertOp: uintXX -> string
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `makeString`
- `v.Uint`
- `string`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtBytesString`
**Signature:** `func cvtBytesString(v Value, t Type)`

**Documentation:**
```go
// convertOp: []byte -> string
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `makeString`
- `v.Bytes`
- `string`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtStringBytes`
**Signature:** `func cvtStringBytes(v Value, t Type)`

**Documentation:**
```go
// convertOp: string -> []byte
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `makeBytes`
- `v.String`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtRunesString`
**Signature:** `func cvtRunesString(v Value, t Type)`

**Documentation:**
```go
// convertOp: []rune -> string
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `makeString`
- `v.runes`
- `string`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtStringRunes`
**Signature:** `func cvtStringRunes(v Value, t Type)`

**Documentation:**
```go
// convertOp: string -> []rune
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `makeRunes`
- `v.String`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtDirect`
**Signature:** `func cvtDirect(v Value, typ Type)`

**Documentation:**
```go
// convertOp: direct copy
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `typedmemmove`
- `typ.common`
- `unsafe_New`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtT2I`
**Signature:** `func cvtT2I(v Value, typ Type)`

**Documentation:**
```go
// convertOp: concrete -> interface
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `flag`
- `typ.NumMethod`
- `typ.common`
- `unsafe_New`
- `valueInterface`
- `ifaceE2I`

#### Called By:
- No incoming calls
</details>

#### Function: `cvtI2I`
**Signature:** `func cvtI2I(v Value, typ Type)`

**Documentation:**
```go
// convertOp: interface -> interface
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `v.IsNil`
- `cvtT2I`
- `Zero`
- `v.Elem`

#### Called By:
- No incoming calls
</details>

#### Function: `chancap`
**Signature:** `func chancap(ch unsafe.Pointer)`

**Documentation:**
```go
// implemented in ../runtime
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `chanclose`
**Signature:** `func chanclose(ch unsafe.Pointer)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `chanlen`
**Signature:** `func chanlen(ch unsafe.Pointer)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `chanrecv`
**Signature:** `func chanrecv(t *rtype, ch unsafe.Pointer, nb bool, val unsafe.Pointer)`

**Documentation:**
```go
//go:noescape
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `chansend`
**Signature:** `func chansend(t *rtype, ch unsafe.Pointer, val unsafe.Pointer, nb bool)`

**Documentation:**
```go
//go:noescape
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `makechan`
**Signature:** `func makechan(typ *rtype, size uint64)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `makemap`
**Signature:** `func makemap(t *rtype)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `mapaccess`
**Signature:** `func mapaccess(t *rtype, m unsafe.Pointer, key unsafe.Pointer)`

**Documentation:**
```go
//go:noescape
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `mapassign`
**Signature:** `func mapassign(t *rtype, m unsafe.Pointer, key, val unsafe.Pointer)`

**Documentation:**
```go
//go:noescape
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `mapdelete`
**Signature:** `func mapdelete(t *rtype, m unsafe.Pointer, key unsafe.Pointer)`

**Documentation:**
```go
//go:noescape
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `mapiterinit`
**Signature:** `func mapiterinit(t *rtype, m unsafe.Pointer)`

**Documentation:**
```go
//go:noescape
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `mapiterkey`
**Signature:** `func mapiterkey(it unsafe.Pointer)`

**Documentation:**
```go
//go:noescape
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `mapiternext`
**Signature:** `func mapiternext(it unsafe.Pointer)`

**Documentation:**
```go
//go:noescape
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `maplen`
**Signature:** `func maplen(m unsafe.Pointer)`

**Documentation:**
```go
//go:noescape
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `call`
**Signature:** `func call(argtype *rtype, fn, arg unsafe.Pointer, n uint32, retoffset uint32)`

**Documentation:**
```go
// call can execute appropriate write barriers during the copy.
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `ifaceE2I`
**Signature:** `func ifaceE2I(t *rtype, src interface{}, dst unsafe.Pointer)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `typedmemmove`
**Signature:** `func typedmemmove(t *rtype, dst, src unsafe.Pointer)`

**Documentation:**
```go
//go:noescape
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `typedmemmovepartial`
**Signature:** `func typedmemmovepartial(t *rtype, dst, src unsafe.Pointer, off, size uintptr)`

**Documentation:**
```go
//go:noescape
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `typedslicecopy`
**Signature:** `func typedslicecopy(elemType *rtype, dst, src sliceHeader)`

**Documentation:**
```go
//go:noescape
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `memclr`
**Signature:** `func memclr(ptr unsafe.Pointer, n uintptr)`

**Documentation:**
```go
//go:noescape
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `escapes`
**Signature:** `func escapes(x interface{})`

**Documentation:**
```go
// the compiler cannot follow.
```

**Operations:**
```go
Makes HTTP requests
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

### File: `letter_test.go`

#### Function: `TestIsLetter`
**Signature:** `func TestIsLetter(t *testing.T)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `t.Errorf`
- `IsLetter`

#### Called By:
- No incoming calls
</details>

#### Function: `TestIsUpper`
**Signature:** `func TestIsUpper(t *testing.T)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `IsUpper`
- `t.Errorf`

#### Called By:
- No incoming calls
</details>

#### Function: `caseString`
**Signature:** `func caseString(c int)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Basic function operations
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `TestTo`
**Signature:** `func TestTo(t *testing.T)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `t.Errorf`
- `caseString`
- `To`

#### Called By:
- No incoming calls
</details>

#### Function: `TestToUpperCase`
**Signature:** `func TestToUpperCase(t *testing.T)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `ToUpper`
- `t.Errorf`

#### Called By:
- No incoming calls
</details>

#### Function: `TestToLowerCase`
**Signature:** `func TestToLowerCase(t *testing.T)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `t.Errorf`
- `ToLower`

#### Called By:
- No incoming calls
</details>

#### Function: `TestToTitleCase`
**Signature:** `func TestToTitleCase(t *testing.T)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `t.Errorf`
- `ToTitle`

#### Called By:
- No incoming calls
</details>

#### Function: `TestIsSpace`
**Signature:** `func TestIsSpace(t *testing.T)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `t.Errorf`
- `IsSpace`

#### Called By:
- No incoming calls
</details>

#### Function: `TestLetterOptimizations`
**Signature:** `func TestLetterOptimizations(t *testing.T)`

**Documentation:**
```go
// We only need to check the Latin-1 range.
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `ToTitle`
- `ToLower`
- `To`
- `t.Errorf`
- `ToUpper`
- `IsSpace`
- `IsLetter`
- `IsTitle`
- `IsUpper`
- `IsLower`
- `rune`
- `Is`

#### Called By:
- No incoming calls
</details>

#### Function: `TestTurkishCase`
**Signature:** `func TestTurkishCase(t *testing.T)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Makes HTTP requests
```

<details>
<summary>Dependencies</summary>

- `t.Errorf`
- `TurkishCase.ToUpper`
- `TurkishCase.ToLower`
- `TurkishCase.ToTitle`

#### Called By:
- No incoming calls
</details>

#### Function: `TestSimpleFold`
**Signature:** `func TestSimpleFold(t *testing.T)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `SimpleFold`
- `len`
- `t.Errorf`

#### Called By:
- No incoming calls
</details>

#### Function: `TestCalibrate`
**Signature:** `func TestCalibrate(t *testing.T)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `linear`
- `binary`
- `bmlinear.NsPerOp`
- `sort.Search`
- `fakeTable`
- `fmt.Printf`
- `testing.Benchmark`
- `uint16`
- `bmbinary.NsPerOp`

#### Called By:
- No incoming calls
</details>

#### Function: `fakeTable`
**Signature:** `func fakeTable(n int)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `append`
- `uint16`

#### Called By:
- No incoming calls
</details>

#### Function: `linear`
**Signature:** `func linear(ranges []Range16, r uint16)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Makes HTTP requests
```

<details>
<summary>Dependencies</summary>

- No outgoing calls

#### Called By:
- No incoming calls
</details>

#### Function: `binary`
**Signature:** `func binary(ranges []Range16, r uint16)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `len`

#### Called By:
- No incoming calls
</details>

#### Function: `TestLatinOffset`
**Signature:** `func TestLatinOffset(t *testing.T)`

**Documentation:**
```go
No documentation available
```

**Operations:**
```go
Performs unit testing and Makes HTTP requests and Handles JSON data and Performs file operations
```

<details>
<summary>Dependencies</summary>

- `t.Errorf`
- `len`

#### Called By:
- No incoming calls
</details>

## Call Stack Visualization

```mermaid
flowchart TD

```
