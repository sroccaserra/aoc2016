"
nc
"
Class {
	#name : #AoC09,
	#superclass : #AoCBase,
	#category : #AoC2016
}

{ #category : #running }
AoC09 >> expandExpressionFrom: i and: aString on: aStream [

	| di expandExp numbers expressionLength partToRepeat |
	di := 1.
	expandExp := String streamContents: [ :s |
		             [
		             | c |
		             c := aString at: i + di.
		             c ~= $) ifTrue: [ s nextPut: c ].
		             di := di + 1.
		             c ~= $) ] whileTrue ].
	numbers := (expandExp substrings: 'x') collect: #asInteger.
	expressionLength := numbers first.
	partToRepeat := aString
		                copyFrom: i + di
		                to: i + di + expressionLength - 1.
	numbers second timesRepeat: [ aStream nextPutAll: partToRepeat ].
	^ di + expressionLength
]

{ #category : #running }
AoC09 >> expandLine: aString [

	^ String streamContents: [ :s | self expandLine: aString on: s ]
]

{ #category : #running }
AoC09 >> expandLine: aString on: aStream [

	| i |
	i := 1.
	[ i <= aString size ] whileTrue: [
		| c |
		c := aString at: i.
		c = $(
			ifTrue: [ i := i + (self expandExpressionFrom: i and: aString on: aStream) ]
			ifFalse: [
				aStream nextPut: (aString at: i).
				i := i + 1 ] ]
]

{ #category : #running }
AoC09 >> run: filename [

	| lines |
	lines := self loadLines: filename.
	^ self solvePartOne: lines
]

{ #category : #running }
AoC09 >> solvePartOne: lines [

	^ ((lines collect: [ :line | self expandLine: line ]) collect: #size)
		  sum
]
