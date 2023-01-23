	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 15
	.globl	_foo
	.p2align	4, 0x90
_foo:
	.cfi_startproc
	pushq	%r14
	.cfi_def_cfa_offset 16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	pushq	%rax
	.cfi_def_cfa_offset 32
	.cfi_offset %rbx, -24
	.cfi_offset %r14, -16
	movabsq	$_ptr, %rbx
	movq	%rdi, (%rbx)
	addb	$13, (%rdi)
	jmp	LBB0_1
	.p2align	4, 0x90
LBB0_1374:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$2, 1(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$5, 3(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$2, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	addq	$-6, (%rbx)
LBB0_1:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1374
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$6, 5(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$-3, 1(%rax)
	movq	(%rbx), %rax
	leaq	10(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$15, 10(%rax)
	jmp	LBB0_3
	.p2align	4, 0x90
LBB0_18:
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	9(%rax)
LBB0_3:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_15
	jmp	LBB0_4
	.p2align	4, 0x90
LBB0_14:
	addq	$9, (%rbx)
LBB0_15:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_14
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_17
	.p2align	4, 0x90
LBB0_19:
	addq	$-9, (%rbx)
LBB0_17:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_19
	jmp	LBB0_18
LBB0_4:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_5
	.p2align	4, 0x90
LBB0_20:
	movq	(%rbx), %rax
	leaq	8(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 8(%rax)
	incq	(%rbx)
LBB0_5:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_20
	.p2align	4, 0x90
LBB0_6:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_6
	movq	(%rbx), %rax
	leaq	8(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 8(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$5, -7(%rax)
	jmp	LBB0_8
	.p2align	4, 0x90
LBB0_23:
	addq	$9, (%rbx)
LBB0_8:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_9
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_22
	.p2align	4, 0x90
LBB0_24:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_22:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_24
	jmp	LBB0_23
LBB0_9:
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	7(%rax)
	movq	(%rbx), %rax
	leaq	27(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	27(%rax)
	addq	$-17, (%rbx)
	jmp	LBB0_10
	.p2align	4, 0x90
LBB0_25:
	addq	$-9, (%rbx)
LBB0_10:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_25
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 3(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	movabsq	$_sys_write, %r14
	jmp	LBB0_12
	.p2align	4, 0x90
LBB0_53:
	addq	$3, (%rbx)
LBB0_12:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_13
	addq	$6, (%rbx)
	jmp	LBB0_27
	.p2align	4, 0x90
LBB0_1375:
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 7(%rax)
	addq	$2, (%rbx)
LBB0_27:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1375
	.p2align	4, 0x90
LBB0_28:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_28
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 7(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$4, -6(%rax)
	jmp	LBB0_30
	.p2align	4, 0x90
LBB0_56:
	addq	$9, (%rbx)
LBB0_30:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_31
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_55
	.p2align	4, 0x90
LBB0_57:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_55:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_57
	jmp	LBB0_56
	.p2align	4, 0x90
LBB0_31:
	movq	(%rbx), %rax
	leaq	6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	6(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$7, -6(%rax)
	jmp	LBB0_32
	.p2align	4, 0x90
LBB0_60:
	addq	$9, (%rbx)
LBB0_32:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_33
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_59
	.p2align	4, 0x90
LBB0_61:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_59:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_61
	jmp	LBB0_60
	.p2align	4, 0x90
LBB0_33:
	movq	(%rbx), %rax
	leaq	6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	6(%rax)
	addq	$-16, (%rbx)
	jmp	LBB0_34
	.p2align	4, 0x90
LBB0_62:
	addq	$-9, (%rbx)
LBB0_34:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_62
	jmp	LBB0_35
	.p2align	4, 0x90
LBB0_63:
	movq	(%rbx), %rax
	movb	$0, (%rax)
	addq	$6, (%rbx)
	jmp	LBB0_64
	.p2align	4, 0x90
LBB0_148:
	addq	$8, (%rbx)
LBB0_64:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_65
	addq	$7, (%rbx)
	jmp	LBB0_145
	.p2align	4, 0x90
LBB0_1376:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-6(%rax)
	addq	$6, (%rbx)
LBB0_145:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1376
	addq	$-6, (%rbx)
	jmp	LBB0_147
	.p2align	4, 0x90
LBB0_149:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	6(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	decq	(%rbx)
LBB0_147:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_149
	jmp	LBB0_148
	.p2align	4, 0x90
LBB0_65:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_65
	addq	$9, (%rbx)
	jmp	LBB0_67
	.p2align	4, 0x90
LBB0_154:
	addq	$8, (%rbx)
LBB0_67:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_68
	addq	$8, (%rbx)
	jmp	LBB0_151
	.p2align	4, 0x90
LBB0_1377:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-7(%rax)
	addq	$7, (%rbx)
LBB0_151:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1377
	addq	$-7, (%rbx)
	jmp	LBB0_153
	.p2align	4, 0x90
LBB0_155:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	7(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	addq	$-2, (%rbx)
LBB0_153:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_155
	jmp	LBB0_154
	.p2align	4, 0x90
LBB0_68:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_68
	jmp	LBB0_69
	.p2align	4, 0x90
LBB0_156:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-7(%rax)
LBB0_69:
	addq	$7, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_156
	addq	$-7, (%rbx)
	jmp	LBB0_71
	.p2align	4, 0x90
LBB0_157:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	7(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	addq	$-5, (%rbx)
LBB0_71:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_157
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$15, 9(%rax)
	jmp	LBB0_73
	.p2align	4, 0x90
LBB0_162:
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	9(%rax)
LBB0_73:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_159
	jmp	LBB0_74
	.p2align	4, 0x90
LBB0_158:
	addq	$9, (%rbx)
LBB0_159:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_158
	movq	(%rbx), %rax
	incb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	.p2align	4, 0x90
LBB0_161:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_161
	jmp	LBB0_162
	.p2align	4, 0x90
LBB0_74:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_75
	.p2align	4, 0x90
LBB0_163:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	addq	$8, (%rbx)
LBB0_75:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_163
	.p2align	4, 0x90
LBB0_76:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_76
	addq	$9, (%rbx)
	jmp	LBB0_78
	.p2align	4, 0x90
LBB0_173:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
	addq	$8, (%rbx)
LBB0_78:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_79
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	jmp	LBB0_165
	.p2align	4, 0x90
LBB0_1378:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
LBB0_165:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1378
	addq	$-4, (%rbx)
	jmp	LBB0_167
	.p2align	4, 0x90
LBB0_174:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$-5, (%rbx)
	jmp	LBB0_175
	.p2align	4, 0x90
LBB0_183:
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$9, (%rbx)
LBB0_175:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_176
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_180
	.p2align	4, 0x90
LBB0_1379:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
LBB0_180:
	addq	$2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1379
	addq	$-2, (%rbx)
	jmp	LBB0_182
	.p2align	4, 0x90
LBB0_184:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	addq	$-4, (%rbx)
LBB0_182:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_184
	jmp	LBB0_183
	.p2align	4, 0x90
LBB0_176:
	addq	$-8, (%rbx)
	jmp	LBB0_177
	.p2align	4, 0x90
LBB0_178:
	addq	$-9, (%rbx)
LBB0_177:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_178
LBB0_167:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_174
	.p2align	4, 0x90
LBB0_168:
	addq	$9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_168
	addq	$-9, (%rbx)
	jmp	LBB0_170
	.p2align	4, 0x90
LBB0_187:
	addq	$-10, (%rbx)
LBB0_170:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_171
	incq	(%rbx)
	jmp	LBB0_186
	.p2align	4, 0x90
LBB0_188:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_186:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_188
	jmp	LBB0_187
	.p2align	4, 0x90
LBB0_171:
	incq	(%rbx)
	jmp	LBB0_172
	.p2align	4, 0x90
LBB0_189:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_172:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_189
	jmp	LBB0_173
	.p2align	4, 0x90
LBB0_193:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
LBB0_79:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_80
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	jmp	LBB0_191
	.p2align	4, 0x90
LBB0_194:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	incq	(%rbx)
	jmp	LBB0_195
	.p2align	4, 0x90
LBB0_1380:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-6(%rax)
	addq	$6, (%rbx)
LBB0_195:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1380
	jmp	LBB0_196
	.p2align	4, 0x90
LBB0_197:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_196:
	decq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_197
LBB0_191:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_194
	jmp	LBB0_192
	.p2align	4, 0x90
LBB0_198:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
LBB0_192:
	addq	$-3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_198
	jmp	LBB0_193
	.p2align	4, 0x90
LBB0_80:
	addq	$9, (%rbx)
	jmp	LBB0_81
	.p2align	4, 0x90
LBB0_199:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	addq	$8, (%rbx)
LBB0_81:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_199
	.p2align	4, 0x90
LBB0_82:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_82
	addq	$9, (%rbx)
	jmp	LBB0_84
	.p2align	4, 0x90
LBB0_209:
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	addq	$8, (%rbx)
LBB0_84:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_85
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	jmp	LBB0_201
	.p2align	4, 0x90
LBB0_1381:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-5(%rax)
LBB0_201:
	addq	$5, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1381
	addq	$-5, (%rbx)
	jmp	LBB0_203
	.p2align	4, 0x90
LBB0_210:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	addq	$-6, (%rbx)
	jmp	LBB0_211
	.p2align	4, 0x90
LBB0_219:
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$9, (%rbx)
LBB0_211:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_212
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_216
	.p2align	4, 0x90
LBB0_1382:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
LBB0_216:
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1382
	addq	$-3, (%rbx)
	jmp	LBB0_218
	.p2align	4, 0x90
LBB0_220:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	addq	$-4, (%rbx)
LBB0_218:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_220
	jmp	LBB0_219
	.p2align	4, 0x90
LBB0_212:
	addq	$-8, (%rbx)
	jmp	LBB0_213
	.p2align	4, 0x90
LBB0_214:
	addq	$-9, (%rbx)
LBB0_213:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_214
LBB0_203:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_210
	.p2align	4, 0x90
LBB0_204:
	addq	$9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_204
	addq	$-9, (%rbx)
	jmp	LBB0_206
	.p2align	4, 0x90
LBB0_223:
	addq	$-11, (%rbx)
LBB0_206:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_207
	addq	$2, (%rbx)
	jmp	LBB0_222
	.p2align	4, 0x90
LBB0_224:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_222:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_224
	jmp	LBB0_223
	.p2align	4, 0x90
LBB0_207:
	addq	$2, (%rbx)
	jmp	LBB0_208
	.p2align	4, 0x90
LBB0_225:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_208:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_225
	jmp	LBB0_209
	.p2align	4, 0x90
LBB0_229:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
LBB0_85:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_86
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	jmp	LBB0_227
	.p2align	4, 0x90
LBB0_230:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	incq	(%rbx)
	jmp	LBB0_231
	.p2align	4, 0x90
LBB0_1383:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-6(%rax)
	addq	$6, (%rbx)
LBB0_231:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1383
	jmp	LBB0_232
	.p2align	4, 0x90
LBB0_233:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_232:
	decq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_233
LBB0_227:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_230
	jmp	LBB0_228
	.p2align	4, 0x90
LBB0_234:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
LBB0_228:
	addq	$-3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_234
	jmp	LBB0_229
	.p2align	4, 0x90
LBB0_86:
	addq	$9, (%rbx)
	jmp	LBB0_87
	.p2align	4, 0x90
LBB0_237:
	addq	$5, (%rbx)
LBB0_87:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_88
	addq	$4, (%rbx)
	jmp	LBB0_236
	.p2align	4, 0x90
LBB0_238:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-36(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-36(%rax)
	addq	$36, (%rbx)
LBB0_236:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_238
	jmp	LBB0_237
	.p2align	4, 0x90
LBB0_88:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_88
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$15, 9(%rax)
	jmp	LBB0_90
	.p2align	4, 0x90
LBB0_243:
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	9(%rax)
LBB0_90:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_240
	jmp	LBB0_91
	.p2align	4, 0x90
LBB0_239:
	addq	$9, (%rbx)
LBB0_240:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_239
	movq	(%rbx), %rax
	leaq	-9(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-9(%rax)
	.p2align	4, 0x90
LBB0_242:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_242
	jmp	LBB0_243
	.p2align	4, 0x90
LBB0_91:
	movq	(%rbx), %rax
	incb	(%rax)
	movq	(%rbx), %rax
	leaq	21(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	21(%rax)
	addq	$-3, (%rbx)
	jmp	LBB0_92
	.p2align	4, 0x90
LBB0_244:
	addq	$-9, (%rbx)
LBB0_92:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_244
	addq	$9, (%rbx)
	jmp	LBB0_94
	.p2align	4, 0x90
LBB0_255:
	addq	$8, (%rbx)
LBB0_94:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_246
	jmp	LBB0_95
	.p2align	4, 0x90
LBB0_245:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-3(%rax)
LBB0_246:
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_245
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-3, (%rbx)
	.p2align	4, 0x90
LBB0_248:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_249
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	incq	(%rbx)
	jmp	LBB0_257
	.p2align	4, 0x90
LBB0_1384:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	addq	$4, (%rbx)
LBB0_257:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1384
	addq	$-4, (%rbx)
	jmp	LBB0_259
	.p2align	4, 0x90
LBB0_264:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	decq	(%rbx)
LBB0_259:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_248
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$-13, (%rbx)
	jmp	LBB0_261
	.p2align	4, 0x90
LBB0_1385:
	addq	$-9, (%rbx)
LBB0_261:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1385
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 4(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_263
	.p2align	4, 0x90
LBB0_265:
	addq	$9, (%rbx)
LBB0_263:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_265
	jmp	LBB0_264
	.p2align	4, 0x90
LBB0_249:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_250
	.p2align	4, 0x90
LBB0_266:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-4(%rax)
LBB0_250:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_266
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-4, (%rbx)
	.p2align	4, 0x90
LBB0_252:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_253
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	4(%rax)
	decq	(%rbx)
	jmp	LBB0_268
	.p2align	4, 0x90
LBB0_1386:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	addq	$3, (%rbx)
LBB0_268:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1386
	addq	$-3, (%rbx)
	jmp	LBB0_270
	.p2align	4, 0x90
LBB0_275:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	decq	(%rbx)
LBB0_270:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_252
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$-12, (%rbx)
	jmp	LBB0_272
	.p2align	4, 0x90
LBB0_1387:
	addq	$-9, (%rbx)
LBB0_272:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1387
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 3(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$6, (%rbx)
	jmp	LBB0_274
	.p2align	4, 0x90
LBB0_276:
	addq	$9, (%rbx)
LBB0_274:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_276
	jmp	LBB0_275
	.p2align	4, 0x90
LBB0_253:
	movq	(%rbx), %rax
	incb	(%rax)
	incq	(%rbx)
	jmp	LBB0_254
	.p2align	4, 0x90
LBB0_279:
	addq	$-8, (%rbx)
LBB0_254:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_255
	movq	(%rbx), %rax
	decb	(%rax)
	decq	(%rbx)
	jmp	LBB0_278
	.p2align	4, 0x90
LBB0_280:
	addq	$9, (%rbx)
LBB0_278:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_280
	jmp	LBB0_279
	.p2align	4, 0x90
LBB0_95:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_95
	addq	$-7, (%rbx)
	jmp	LBB0_97
	.p2align	4, 0x90
LBB0_281:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	addq	$-4, (%rbx)
LBB0_97:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_281
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$26, 9(%rax)
	addq	$2, (%rbx)
	jmp	LBB0_99
	.p2align	4, 0x90
LBB0_282:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	addq	$4, (%rbx)
LBB0_99:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_282
	addq	$-4, (%rbx)
	jmp	LBB0_101
	.p2align	4, 0x90
LBB0_283:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, -2(%rax)
	addq	$-2, (%rbx)
LBB0_101:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_283
	jmp	LBB0_102
	.p2align	4, 0x90
LBB0_284:
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-7(%rax)
	decq	(%rbx)
	jmp	LBB0_285
	.p2align	4, 0x90
LBB0_1388:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, -2(%rax)
LBB0_285:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1388
	incq	(%rbx)
	jmp	LBB0_287
	.p2align	4, 0x90
LBB0_426:
	addq	$3, (%rbx)
LBB0_287:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_288
	movq	(%rbx), %rax
	decb	(%rax)
	addq	$-2, (%rbx)
	jmp	LBB0_425
	.p2align	4, 0x90
LBB0_427:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	addq	$-4, (%rbx)
LBB0_425:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_427
	jmp	LBB0_426
	.p2align	4, 0x90
LBB0_288:
	addq	$13, (%rbx)
	jmp	LBB0_289
	.p2align	4, 0x90
LBB0_428:
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 2(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	addq	$5, (%rbx)
LBB0_289:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_428
	.p2align	4, 0x90
LBB0_290:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_290
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 3(%rax)
	addq	$6, (%rbx)
	jmp	LBB0_292
	.p2align	4, 0x90
LBB0_433:
	addq	$8, (%rbx)
LBB0_292:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_293
	addq	$5, (%rbx)
	jmp	LBB0_430
	.p2align	4, 0x90
LBB0_1389:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	addq	$4, (%rbx)
LBB0_430:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1389
	addq	$-4, (%rbx)
	jmp	LBB0_432
	.p2align	4, 0x90
LBB0_434:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	decq	(%rbx)
LBB0_432:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_434
	jmp	LBB0_433
	.p2align	4, 0x90
LBB0_293:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_293
	addq	$9, (%rbx)
	jmp	LBB0_295
	.p2align	4, 0x90
LBB0_437:
	addq	$7, (%rbx)
LBB0_295:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_296
	addq	$2, (%rbx)
	jmp	LBB0_436
	.p2align	4, 0x90
LBB0_438:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-9(%rax)
	addq	$9, (%rbx)
LBB0_436:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_438
	jmp	LBB0_437
	.p2align	4, 0x90
LBB0_296:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_296
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$15, 9(%rax)
	jmp	LBB0_298
	.p2align	4, 0x90
LBB0_443:
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	9(%rax)
LBB0_298:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_440
	jmp	LBB0_299
	.p2align	4, 0x90
LBB0_439:
	addq	$9, (%rbx)
LBB0_440:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_439
	movq	(%rbx), %rax
	incb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	.p2align	4, 0x90
LBB0_442:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_442
	jmp	LBB0_443
	.p2align	4, 0x90
LBB0_299:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_300
	.p2align	4, 0x90
LBB0_444:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	addq	$8, (%rbx)
LBB0_300:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_444
	.p2align	4, 0x90
LBB0_301:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_301
	addq	$9, (%rbx)
	jmp	LBB0_303
	.p2align	4, 0x90
LBB0_454:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
	addq	$8, (%rbx)
LBB0_303:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_304
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	jmp	LBB0_446
	.p2align	4, 0x90
LBB0_1390:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-5(%rax)
LBB0_446:
	addq	$5, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1390
	addq	$-5, (%rbx)
	jmp	LBB0_448
	.p2align	4, 0x90
LBB0_455:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	addq	$-6, (%rbx)
	jmp	LBB0_456
	.p2align	4, 0x90
LBB0_464:
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$9, (%rbx)
LBB0_456:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_457
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_461
	.p2align	4, 0x90
LBB0_1391:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
LBB0_461:
	addq	$2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1391
	addq	$-2, (%rbx)
	jmp	LBB0_463
	.p2align	4, 0x90
LBB0_465:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	addq	$-3, (%rbx)
LBB0_463:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_465
	jmp	LBB0_464
	.p2align	4, 0x90
LBB0_457:
	addq	$-8, (%rbx)
	jmp	LBB0_458
	.p2align	4, 0x90
LBB0_459:
	addq	$-9, (%rbx)
LBB0_458:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_459
LBB0_448:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_455
	.p2align	4, 0x90
LBB0_449:
	addq	$9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_449
	addq	$-9, (%rbx)
	jmp	LBB0_451
	.p2align	4, 0x90
LBB0_468:
	addq	$-10, (%rbx)
LBB0_451:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_452
	incq	(%rbx)
	jmp	LBB0_467
	.p2align	4, 0x90
LBB0_469:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_467:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_469
	jmp	LBB0_468
	.p2align	4, 0x90
LBB0_452:
	incq	(%rbx)
	jmp	LBB0_453
	.p2align	4, 0x90
LBB0_470:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_453:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_470
	jmp	LBB0_454
	.p2align	4, 0x90
LBB0_474:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
LBB0_304:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_305
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	jmp	LBB0_472
	.p2align	4, 0x90
LBB0_475:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	incq	(%rbx)
	jmp	LBB0_476
	.p2align	4, 0x90
LBB0_1392:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-7(%rax)
	addq	$7, (%rbx)
LBB0_476:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1392
	jmp	LBB0_477
	.p2align	4, 0x90
LBB0_478:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_477:
	decq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_478
LBB0_472:
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_475
	jmp	LBB0_473
	.p2align	4, 0x90
LBB0_479:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
LBB0_473:
	addq	$-2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_479
	jmp	LBB0_474
	.p2align	4, 0x90
LBB0_305:
	addq	$9, (%rbx)
	jmp	LBB0_306
	.p2align	4, 0x90
LBB0_484:
	addq	$8, (%rbx)
LBB0_306:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_307
	addq	$6, (%rbx)
	jmp	LBB0_481
	.p2align	4, 0x90
LBB0_1393:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-5(%rax)
	addq	$5, (%rbx)
LBB0_481:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1393
	addq	$-5, (%rbx)
	jmp	LBB0_483
	.p2align	4, 0x90
LBB0_485:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	decq	(%rbx)
LBB0_483:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_485
	jmp	LBB0_484
	.p2align	4, 0x90
LBB0_307:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_307
	addq	$9, (%rbx)
	jmp	LBB0_309
	.p2align	4, 0x90
LBB0_486:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	addq	$8, (%rbx)
LBB0_309:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_486
	.p2align	4, 0x90
LBB0_310:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_310
	addq	$9, (%rbx)
	jmp	LBB0_312
	.p2align	4, 0x90
LBB0_496:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
	addq	$8, (%rbx)
LBB0_312:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_313
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	jmp	LBB0_488
	.p2align	4, 0x90
LBB0_1394:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-5(%rax)
LBB0_488:
	addq	$5, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1394
	addq	$-5, (%rbx)
	jmp	LBB0_490
	.p2align	4, 0x90
LBB0_497:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	addq	$-6, (%rbx)
	jmp	LBB0_498
	.p2align	4, 0x90
LBB0_506:
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$9, (%rbx)
LBB0_498:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_499
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_503
	.p2align	4, 0x90
LBB0_1395:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
LBB0_503:
	addq	$2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1395
	addq	$-2, (%rbx)
	jmp	LBB0_505
	.p2align	4, 0x90
LBB0_507:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	addq	$-4, (%rbx)
LBB0_505:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_507
	jmp	LBB0_506
	.p2align	4, 0x90
LBB0_499:
	addq	$-8, (%rbx)
	jmp	LBB0_500
	.p2align	4, 0x90
LBB0_501:
	addq	$-9, (%rbx)
LBB0_500:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_501
LBB0_490:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_497
	.p2align	4, 0x90
LBB0_491:
	addq	$9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_491
	addq	$-9, (%rbx)
	jmp	LBB0_493
	.p2align	4, 0x90
LBB0_510:
	addq	$-10, (%rbx)
LBB0_493:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_494
	incq	(%rbx)
	jmp	LBB0_509
	.p2align	4, 0x90
LBB0_511:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_509:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_511
	jmp	LBB0_510
	.p2align	4, 0x90
LBB0_494:
	incq	(%rbx)
	jmp	LBB0_495
	.p2align	4, 0x90
LBB0_512:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_495:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_512
	jmp	LBB0_496
	.p2align	4, 0x90
LBB0_516:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
LBB0_313:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_314
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	jmp	LBB0_514
	.p2align	4, 0x90
LBB0_517:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	incq	(%rbx)
	jmp	LBB0_518
	.p2align	4, 0x90
LBB0_1396:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-6(%rax)
	addq	$6, (%rbx)
LBB0_518:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1396
	jmp	LBB0_519
	.p2align	4, 0x90
LBB0_520:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_519:
	decq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_520
LBB0_514:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_517
	jmp	LBB0_515
	.p2align	4, 0x90
LBB0_521:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
LBB0_515:
	addq	$-3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_521
	jmp	LBB0_516
	.p2align	4, 0x90
LBB0_314:
	addq	$9, (%rbx)
	jmp	LBB0_315
	.p2align	4, 0x90
LBB0_524:
	addq	$5, (%rbx)
LBB0_315:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_316
	addq	$4, (%rbx)
	jmp	LBB0_523
	.p2align	4, 0x90
LBB0_525:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-36(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-36(%rax)
	addq	$36, (%rbx)
LBB0_523:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_525
	jmp	LBB0_524
	.p2align	4, 0x90
LBB0_316:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_316
	addq	$9, (%rbx)
	jmp	LBB0_318
	.p2align	4, 0x90
LBB0_528:
	addq	$6, (%rbx)
LBB0_318:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_319
	addq	$3, (%rbx)
	jmp	LBB0_527
	.p2align	4, 0x90
LBB0_529:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-36(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-36(%rax)
	addq	$36, (%rbx)
LBB0_527:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_529
	jmp	LBB0_528
	.p2align	4, 0x90
LBB0_319:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_319
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$15, 9(%rax)
	jmp	LBB0_321
	.p2align	4, 0x90
LBB0_534:
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	9(%rax)
LBB0_321:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_531
	jmp	LBB0_322
	.p2align	4, 0x90
LBB0_530:
	addq	$9, (%rbx)
LBB0_531:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_530
	movq	(%rbx), %rax
	leaq	-9(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-9(%rax)
	.p2align	4, 0x90
LBB0_533:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_533
	jmp	LBB0_534
	.p2align	4, 0x90
LBB0_322:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_323
	.p2align	4, 0x90
LBB0_539:
	addq	$8, (%rbx)
LBB0_323:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_324
	addq	$8, (%rbx)
	jmp	LBB0_536
	.p2align	4, 0x90
LBB0_1397:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-7(%rax)
	addq	$7, (%rbx)
LBB0_536:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1397
	addq	$-7, (%rbx)
	jmp	LBB0_538
	.p2align	4, 0x90
LBB0_540:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	7(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-6(%rax)
	decq	(%rbx)
LBB0_538:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_540
	jmp	LBB0_539
	.p2align	4, 0x90
LBB0_324:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_324
	addq	$9, (%rbx)
	jmp	LBB0_326
	.p2align	4, 0x90
LBB0_541:
	movq	(%rbx), %rax
	leaq	6(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 6(%rax)
	addq	$3, (%rbx)
LBB0_326:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_541
	.p2align	4, 0x90
LBB0_327:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_327
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	incq	(%rbx)
	jmp	LBB0_329
	.p2align	4, 0x90
LBB0_542:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	addq	$5, (%rbx)
LBB0_329:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_542
	jmp	LBB0_330
	.p2align	4, 0x90
LBB0_546:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_330:
	incq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_331
	movq	(%rbx), %rax
	decb	(%rax)
	addq	$-6, (%rbx)
	jmp	LBB0_544
	.p2align	4, 0x90
LBB0_1398:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$2, -1(%rax)
	addq	$-4, (%rbx)
LBB0_544:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1398
	jmp	LBB0_545
	.p2align	4, 0x90
LBB0_547:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-5(%rax)
LBB0_545:
	addq	$5, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_547
	jmp	LBB0_546
	.p2align	4, 0x90
LBB0_548:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_331:
	decq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_548
	jmp	LBB0_332
	.p2align	4, 0x90
LBB0_549:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
LBB0_332:
	addq	$-5, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_549
	movq	(%rbx), %rax
	leaq	6(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 6(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-6(%rax)
	jmp	LBB0_334
	.p2align	4, 0x90
LBB0_550:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-4(%rax)
LBB0_334:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_550
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-4, (%rbx)
	.p2align	4, 0x90
LBB0_336:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_337
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	4(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_552
	.p2align	4, 0x90
LBB0_574:
	addq	$8, (%rbx)
LBB0_552:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_565
	jmp	LBB0_553
	.p2align	4, 0x90
LBB0_564:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-2(%rax)
LBB0_565:
	addq	$2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_564
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-2, (%rbx)
	.p2align	4, 0x90
LBB0_567:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_568
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	2(%rax)
	incq	(%rbx)
	jmp	LBB0_576
	.p2align	4, 0x90
LBB0_1399:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	addq	$3, (%rbx)
LBB0_576:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1399
	addq	$-3, (%rbx)
	jmp	LBB0_578
	.p2align	4, 0x90
LBB0_583:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	decq	(%rbx)
LBB0_578:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_567
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$-12, (%rbx)
	jmp	LBB0_580
	.p2align	4, 0x90
LBB0_1400:
	addq	$-9, (%rbx)
LBB0_580:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1400
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 3(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$6, (%rbx)
	jmp	LBB0_582
	.p2align	4, 0x90
LBB0_584:
	addq	$9, (%rbx)
LBB0_582:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_584
	jmp	LBB0_583
	.p2align	4, 0x90
LBB0_568:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_569
	.p2align	4, 0x90
LBB0_585:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-3(%rax)
LBB0_569:
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_585
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-3, (%rbx)
	.p2align	4, 0x90
LBB0_571:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_572
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	decq	(%rbx)
	jmp	LBB0_587
	.p2align	4, 0x90
LBB0_1401:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	addq	$2, (%rbx)
LBB0_587:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1401
	addq	$-2, (%rbx)
	jmp	LBB0_589
	.p2align	4, 0x90
LBB0_594:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	decq	(%rbx)
LBB0_589:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_571
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	addq	$-11, (%rbx)
	jmp	LBB0_591
	.p2align	4, 0x90
LBB0_1402:
	addq	$-9, (%rbx)
LBB0_591:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1402
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 4(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_593
	.p2align	4, 0x90
LBB0_595:
	addq	$9, (%rbx)
LBB0_593:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_595
	jmp	LBB0_594
	.p2align	4, 0x90
LBB0_572:
	movq	(%rbx), %rax
	incb	(%rax)
	incq	(%rbx)
	jmp	LBB0_573
	.p2align	4, 0x90
LBB0_598:
	addq	$-8, (%rbx)
LBB0_573:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_574
	movq	(%rbx), %rax
	decb	(%rax)
	decq	(%rbx)
	jmp	LBB0_597
	.p2align	4, 0x90
LBB0_599:
	addq	$9, (%rbx)
LBB0_597:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_599
	jmp	LBB0_598
	.p2align	4, 0x90
LBB0_553:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_553
	jmp	LBB0_554
	.p2align	4, 0x90
LBB0_600:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
LBB0_554:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_600
	jmp	LBB0_555
	.p2align	4, 0x90
LBB0_605:
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 4(%rax)
LBB0_555:
	addq	$-4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_556
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_602
	.p2align	4, 0x90
LBB0_609:
	addq	$8, (%rbx)
LBB0_602:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_603
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	jmp	LBB0_607
	.p2align	4, 0x90
LBB0_1403:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-2(%rax)
LBB0_607:
	addq	$2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1403
	jmp	LBB0_608
	.p2align	4, 0x90
LBB0_610:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
LBB0_608:
	addq	$-2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_610
	jmp	LBB0_609
	.p2align	4, 0x90
LBB0_603:
	movq	(%rbx), %rax
	leaq	-8(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-8(%rax)
	decq	(%rbx)
	jmp	LBB0_604
	.p2align	4, 0x90
LBB0_617:
	addq	$-12, (%rbx)
LBB0_604:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_605
	incq	(%rbx)
	jmp	LBB0_612
	.p2align	4, 0x90
LBB0_622:
	addq	$-2, (%rbx)
LBB0_612:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_613
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	addq	$-4, (%rbx)
	jmp	LBB0_619
	.p2align	4, 0x90
LBB0_625:
	decq	(%rbx)
LBB0_619:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_620
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	4(%rax)
	movq	(%rbx), %rax
	leaq	-14(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-14(%rax)
	addq	$11, (%rbx)
	jmp	LBB0_624
	.p2align	4, 0x90
LBB0_626:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$-3, (%rbx)
LBB0_624:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_626
	jmp	LBB0_625
	.p2align	4, 0x90
LBB0_620:
	incq	(%rbx)
	jmp	LBB0_621
	.p2align	4, 0x90
LBB0_627:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	movq	(%rbx), %rax
	leaq	-14(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-14(%rax)
	addq	$11, (%rbx)
LBB0_621:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_627
	jmp	LBB0_622
	.p2align	4, 0x90
LBB0_613:
	incq	(%rbx)
	jmp	LBB0_614
	.p2align	4, 0x90
LBB0_630:
	decq	(%rbx)
LBB0_614:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_615
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$-3, (%rbx)
	jmp	LBB0_629
	.p2align	4, 0x90
LBB0_631:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	movq	(%rbx), %rax
	leaq	-14(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-14(%rax)
	addq	$11, (%rbx)
LBB0_629:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_631
	jmp	LBB0_630
	.p2align	4, 0x90
LBB0_615:
	incq	(%rbx)
	jmp	LBB0_616
	.p2align	4, 0x90
LBB0_632:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$-3, (%rbx)
LBB0_616:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_632
	jmp	LBB0_617
	.p2align	4, 0x90
LBB0_633:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
LBB0_556:
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_633
	addq	$-3, (%rbx)
	jmp	LBB0_558
	.p2align	4, 0x90
LBB0_563:
	movq	(%rbx), %rax
	leaq	6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	6(%rax)
	addq	$-6, (%rbx)
LBB0_558:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_336
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$6, (%rbx)
	jmp	LBB0_560
	.p2align	4, 0x90
LBB0_637:
	addq	$8, (%rbx)
LBB0_560:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_561
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	jmp	LBB0_635
	.p2align	4, 0x90
LBB0_1404:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
LBB0_635:
	incq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1404
	jmp	LBB0_636
	.p2align	4, 0x90
LBB0_638:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_636:
	decq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_638
	jmp	LBB0_637
	.p2align	4, 0x90
LBB0_561:
	movq	(%rbx), %rax
	leaq	-8(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-8(%rax)
	decq	(%rbx)
	jmp	LBB0_562
	.p2align	4, 0x90
LBB0_645:
	addq	$-11, (%rbx)
LBB0_562:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_563
	incq	(%rbx)
	jmp	LBB0_640
	.p2align	4, 0x90
LBB0_650:
	decq	(%rbx)
LBB0_640:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_641
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	addq	$-3, (%rbx)
	jmp	LBB0_647
	.p2align	4, 0x90
LBB0_653:
	incq	(%rbx)
LBB0_647:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_648
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	movq	(%rbx), %rax
	leaq	-14(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-14(%rax)
	addq	$10, (%rbx)
	jmp	LBB0_652
	.p2align	4, 0x90
LBB0_654:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$-4, (%rbx)
LBB0_652:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_654
	jmp	LBB0_653
	.p2align	4, 0x90
LBB0_648:
	decq	(%rbx)
	jmp	LBB0_649
	.p2align	4, 0x90
LBB0_655:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	4(%rax)
	movq	(%rbx), %rax
	leaq	-14(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-14(%rax)
	addq	$10, (%rbx)
LBB0_649:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_655
	jmp	LBB0_650
	.p2align	4, 0x90
LBB0_641:
	addq	$2, (%rbx)
	jmp	LBB0_642
	.p2align	4, 0x90
LBB0_658:
	incq	(%rbx)
LBB0_642:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_643
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$-4, (%rbx)
	jmp	LBB0_657
	.p2align	4, 0x90
LBB0_659:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	4(%rax)
	movq	(%rbx), %rax
	leaq	-14(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-14(%rax)
	addq	$10, (%rbx)
LBB0_657:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_659
	jmp	LBB0_658
	.p2align	4, 0x90
LBB0_643:
	decq	(%rbx)
	jmp	LBB0_644
	.p2align	4, 0x90
LBB0_660:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$-4, (%rbx)
LBB0_644:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_660
	jmp	LBB0_645
	.p2align	4, 0x90
LBB0_661:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
LBB0_337:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_661
	addq	$-4, (%rbx)
	.p2align	4, 0x90
LBB0_339:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_340
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_663
	.p2align	4, 0x90
LBB0_1405:
	addq	$9, (%rbx)
LBB0_663:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1405
	addq	$-9, (%rbx)
	jmp	LBB0_665
	.p2align	4, 0x90
LBB0_672:
	addq	$-12, (%rbx)
LBB0_665:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_339
	incq	(%rbx)
	jmp	LBB0_667
	.p2align	4, 0x90
LBB0_677:
	addq	$-2, (%rbx)
LBB0_667:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_668
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	addq	$-4, (%rbx)
	jmp	LBB0_674
	.p2align	4, 0x90
LBB0_680:
	decq	(%rbx)
LBB0_674:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_675
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	4(%rax)
	movq	(%rbx), %rax
	leaq	-14(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-14(%rax)
	addq	$11, (%rbx)
	jmp	LBB0_679
	.p2align	4, 0x90
LBB0_681:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$-3, (%rbx)
LBB0_679:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_681
	jmp	LBB0_680
	.p2align	4, 0x90
LBB0_675:
	incq	(%rbx)
	jmp	LBB0_676
	.p2align	4, 0x90
LBB0_682:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	movq	(%rbx), %rax
	leaq	-14(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-14(%rax)
	addq	$11, (%rbx)
LBB0_676:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_682
	jmp	LBB0_677
	.p2align	4, 0x90
LBB0_668:
	incq	(%rbx)
	jmp	LBB0_669
	.p2align	4, 0x90
LBB0_685:
	decq	(%rbx)
LBB0_669:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_670
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$-3, (%rbx)
	jmp	LBB0_684
	.p2align	4, 0x90
LBB0_686:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	movq	(%rbx), %rax
	leaq	-14(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-14(%rax)
	addq	$11, (%rbx)
LBB0_684:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_686
	jmp	LBB0_685
	.p2align	4, 0x90
LBB0_670:
	incq	(%rbx)
	jmp	LBB0_671
	.p2align	4, 0x90
LBB0_687:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$-3, (%rbx)
LBB0_671:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_687
	jmp	LBB0_672
	.p2align	4, 0x90
LBB0_340:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 2(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_341
	.p2align	4, 0x90
LBB0_688:
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 2(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	addq	$6, (%rbx)
LBB0_341:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_688
	.p2align	4, 0x90
LBB0_342:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_342
	addq	$9, (%rbx)
	jmp	LBB0_344
	.p2align	4, 0x90
LBB0_693:
	addq	$8, (%rbx)
LBB0_344:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_345
	addq	$5, (%rbx)
	jmp	LBB0_690
	.p2align	4, 0x90
LBB0_1406:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	addq	$4, (%rbx)
LBB0_690:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1406
	addq	$-4, (%rbx)
	jmp	LBB0_692
	.p2align	4, 0x90
LBB0_694:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	decq	(%rbx)
LBB0_692:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_694
	jmp	LBB0_693
	.p2align	4, 0x90
LBB0_345:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_345
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$15, 9(%rax)
	jmp	LBB0_347
	.p2align	4, 0x90
LBB0_699:
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	9(%rax)
LBB0_347:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_696
	jmp	LBB0_348
	.p2align	4, 0x90
LBB0_695:
	addq	$9, (%rbx)
LBB0_696:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_695
	movq	(%rbx), %rax
	incb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	.p2align	4, 0x90
LBB0_698:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_698
	jmp	LBB0_699
	.p2align	4, 0x90
LBB0_348:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_349
	.p2align	4, 0x90
LBB0_700:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	addq	$8, (%rbx)
LBB0_349:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_700
	.p2align	4, 0x90
LBB0_350:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_350
	addq	$9, (%rbx)
	jmp	LBB0_352
	.p2align	4, 0x90
LBB0_710:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
	addq	$8, (%rbx)
LBB0_352:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_353
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	jmp	LBB0_702
	.p2align	4, 0x90
LBB0_1407:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
LBB0_702:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1407
	addq	$-4, (%rbx)
	jmp	LBB0_704
	.p2align	4, 0x90
LBB0_711:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$-5, (%rbx)
	jmp	LBB0_712
	.p2align	4, 0x90
LBB0_720:
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$9, (%rbx)
LBB0_712:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_713
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_717
	.p2align	4, 0x90
LBB0_1408:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
LBB0_717:
	addq	$2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1408
	addq	$-2, (%rbx)
	jmp	LBB0_719
	.p2align	4, 0x90
LBB0_721:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	addq	$-3, (%rbx)
LBB0_719:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_721
	jmp	LBB0_720
	.p2align	4, 0x90
LBB0_713:
	addq	$-8, (%rbx)
	jmp	LBB0_714
	.p2align	4, 0x90
LBB0_715:
	addq	$-9, (%rbx)
LBB0_714:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_715
LBB0_704:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_711
	.p2align	4, 0x90
LBB0_705:
	addq	$9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_705
	addq	$-9, (%rbx)
	jmp	LBB0_707
	.p2align	4, 0x90
LBB0_724:
	addq	$-10, (%rbx)
LBB0_707:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_708
	incq	(%rbx)
	jmp	LBB0_723
	.p2align	4, 0x90
LBB0_725:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_723:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_725
	jmp	LBB0_724
	.p2align	4, 0x90
LBB0_708:
	incq	(%rbx)
	jmp	LBB0_709
	.p2align	4, 0x90
LBB0_726:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_709:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_726
	jmp	LBB0_710
	.p2align	4, 0x90
LBB0_730:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
LBB0_353:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_354
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	jmp	LBB0_728
	.p2align	4, 0x90
LBB0_731:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	incq	(%rbx)
	jmp	LBB0_732
	.p2align	4, 0x90
LBB0_1409:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-7(%rax)
	addq	$7, (%rbx)
LBB0_732:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1409
	jmp	LBB0_733
	.p2align	4, 0x90
LBB0_734:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_733:
	decq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_734
LBB0_728:
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_731
	jmp	LBB0_729
	.p2align	4, 0x90
LBB0_735:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
LBB0_729:
	addq	$-2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_735
	jmp	LBB0_730
	.p2align	4, 0x90
LBB0_354:
	addq	$9, (%rbx)
	jmp	LBB0_355
	.p2align	4, 0x90
LBB0_738:
	addq	$6, (%rbx)
LBB0_355:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_356
	addq	$3, (%rbx)
	jmp	LBB0_737
	.p2align	4, 0x90
LBB0_739:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-36(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-36(%rax)
	addq	$36, (%rbx)
LBB0_737:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_739
	jmp	LBB0_738
	.p2align	4, 0x90
LBB0_356:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_356
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 5(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$15, 4(%rax)
	jmp	LBB0_358
	.p2align	4, 0x90
LBB0_744:
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	9(%rax)
LBB0_358:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_741
	jmp	LBB0_359
	.p2align	4, 0x90
LBB0_740:
	addq	$9, (%rbx)
LBB0_741:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_740
	movq	(%rbx), %rax
	leaq	-9(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-9(%rax)
	.p2align	4, 0x90
LBB0_743:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_743
	jmp	LBB0_744
	.p2align	4, 0x90
LBB0_359:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_360
	.p2align	4, 0x90
LBB0_755:
	addq	$8, (%rbx)
LBB0_360:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_746
	jmp	LBB0_361
	.p2align	4, 0x90
LBB0_745:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-3(%rax)
LBB0_746:
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_745
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-3, (%rbx)
	.p2align	4, 0x90
LBB0_748:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_749
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	incq	(%rbx)
	jmp	LBB0_757
	.p2align	4, 0x90
LBB0_1410:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	addq	$4, (%rbx)
LBB0_757:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1410
	addq	$-4, (%rbx)
	jmp	LBB0_759
	.p2align	4, 0x90
LBB0_764:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	decq	(%rbx)
LBB0_759:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_748
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$-13, (%rbx)
	jmp	LBB0_761
	.p2align	4, 0x90
LBB0_1411:
	addq	$-9, (%rbx)
LBB0_761:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1411
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 4(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_763
	.p2align	4, 0x90
LBB0_765:
	addq	$9, (%rbx)
LBB0_763:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_765
	jmp	LBB0_764
	.p2align	4, 0x90
LBB0_749:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_750
	.p2align	4, 0x90
LBB0_766:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-4(%rax)
LBB0_750:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_766
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-4, (%rbx)
	.p2align	4, 0x90
LBB0_752:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_753
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	4(%rax)
	decq	(%rbx)
	jmp	LBB0_768
	.p2align	4, 0x90
LBB0_1412:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	addq	$3, (%rbx)
LBB0_768:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1412
	addq	$-3, (%rbx)
	jmp	LBB0_770
	.p2align	4, 0x90
LBB0_775:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	decq	(%rbx)
LBB0_770:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_752
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$-12, (%rbx)
	jmp	LBB0_772
	.p2align	4, 0x90
LBB0_1413:
	addq	$-9, (%rbx)
LBB0_772:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1413
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 3(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$6, (%rbx)
	jmp	LBB0_774
	.p2align	4, 0x90
LBB0_776:
	addq	$9, (%rbx)
LBB0_774:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_776
	jmp	LBB0_775
	.p2align	4, 0x90
LBB0_753:
	movq	(%rbx), %rax
	incb	(%rax)
	incq	(%rbx)
	jmp	LBB0_754
	.p2align	4, 0x90
LBB0_779:
	addq	$-8, (%rbx)
LBB0_754:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_755
	movq	(%rbx), %rax
	decb	(%rax)
	decq	(%rbx)
	jmp	LBB0_778
	.p2align	4, 0x90
LBB0_780:
	addq	$9, (%rbx)
LBB0_778:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_780
	jmp	LBB0_779
	.p2align	4, 0x90
LBB0_361:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_361
	jmp	LBB0_362
	.p2align	4, 0x90
LBB0_781:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
LBB0_362:
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_781
	addq	$-3, (%rbx)
	.p2align	4, 0x90
LBB0_364:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_365
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$6, (%rbx)
	jmp	LBB0_783
	.p2align	4, 0x90
LBB0_796:
	addq	$8, (%rbx)
LBB0_783:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_784
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	jmp	LBB0_794
	.p2align	4, 0x90
LBB0_1414:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-3(%rax)
LBB0_794:
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1414
	jmp	LBB0_795
	.p2align	4, 0x90
LBB0_797:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
LBB0_795:
	addq	$-3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_797
	jmp	LBB0_796
	.p2align	4, 0x90
LBB0_784:
	movq	(%rbx), %rax
	leaq	-8(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-8(%rax)
	decq	(%rbx)
	jmp	LBB0_785
	.p2align	4, 0x90
LBB0_792:
	addq	$-13, (%rbx)
LBB0_785:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_364
	incq	(%rbx)
	jmp	LBB0_787
	.p2align	4, 0x90
LBB0_802:
	addq	$-3, (%rbx)
LBB0_787:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_788
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	incq	(%rbx)
	jmp	LBB0_799
	.p2align	4, 0x90
LBB0_805:
	decq	(%rbx)
LBB0_799:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_800
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	-10(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-10(%rax)
	addq	$12, (%rbx)
	jmp	LBB0_804
	.p2align	4, 0x90
LBB0_806:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	addq	$2, (%rbx)
LBB0_804:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_806
	jmp	LBB0_805
	.p2align	4, 0x90
LBB0_800:
	incq	(%rbx)
	jmp	LBB0_801
	.p2align	4, 0x90
LBB0_807:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-2(%rax)
	movq	(%rbx), %rax
	leaq	-10(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-10(%rax)
	addq	$12, (%rbx)
LBB0_801:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_807
	jmp	LBB0_802
	.p2align	4, 0x90
LBB0_788:
	addq	$2, (%rbx)
	jmp	LBB0_789
	.p2align	4, 0x90
LBB0_810:
	decq	(%rbx)
LBB0_789:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_790
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
	addq	$2, (%rbx)
	jmp	LBB0_809
	.p2align	4, 0x90
LBB0_811:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-2(%rax)
	movq	(%rbx), %rax
	leaq	-10(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-10(%rax)
	addq	$12, (%rbx)
LBB0_809:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_811
	jmp	LBB0_810
	.p2align	4, 0x90
LBB0_790:
	incq	(%rbx)
	jmp	LBB0_791
	.p2align	4, 0x90
LBB0_812:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	addq	$2, (%rbx)
LBB0_791:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_812
	jmp	LBB0_792
	.p2align	4, 0x90
LBB0_813:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
LBB0_365:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_813
	addq	$-4, (%rbx)
	jmp	LBB0_367
	.p2align	4, 0x90
LBB0_818:
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	addq	$-5, (%rbx)
LBB0_367:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_368
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_815
	.p2align	4, 0x90
LBB0_822:
	addq	$8, (%rbx)
LBB0_815:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_816
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	jmp	LBB0_820
	.p2align	4, 0x90
LBB0_1415:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-2(%rax)
LBB0_820:
	addq	$2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1415
	jmp	LBB0_821
	.p2align	4, 0x90
LBB0_823:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
LBB0_821:
	addq	$-2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_823
	jmp	LBB0_822
	.p2align	4, 0x90
LBB0_816:
	movq	(%rbx), %rax
	leaq	-8(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-8(%rax)
	decq	(%rbx)
	jmp	LBB0_817
	.p2align	4, 0x90
LBB0_830:
	addq	$-12, (%rbx)
LBB0_817:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_818
	incq	(%rbx)
	jmp	LBB0_825
	.p2align	4, 0x90
LBB0_835:
	addq	$-2, (%rbx)
LBB0_825:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_826
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	addq	$2, (%rbx)
	jmp	LBB0_832
	.p2align	4, 0x90
LBB0_838:
	incq	(%rbx)
LBB0_832:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_833
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-2(%rax)
	movq	(%rbx), %rax
	leaq	-10(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-10(%rax)
	addq	$11, (%rbx)
	jmp	LBB0_837
	.p2align	4, 0x90
LBB0_839:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
	incq	(%rbx)
LBB0_837:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_839
	jmp	LBB0_838
	.p2align	4, 0x90
LBB0_833:
	decq	(%rbx)
	jmp	LBB0_834
	.p2align	4, 0x90
LBB0_840:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	-10(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-10(%rax)
	addq	$11, (%rbx)
LBB0_834:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_840
	jmp	LBB0_835
	.p2align	4, 0x90
LBB0_826:
	addq	$3, (%rbx)
	jmp	LBB0_827
	.p2align	4, 0x90
LBB0_843:
	incq	(%rbx)
LBB0_827:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_828
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	incq	(%rbx)
	jmp	LBB0_842
	.p2align	4, 0x90
LBB0_844:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	-10(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-10(%rax)
	addq	$11, (%rbx)
LBB0_842:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_844
	jmp	LBB0_843
	.p2align	4, 0x90
LBB0_828:
	decq	(%rbx)
	jmp	LBB0_829
	.p2align	4, 0x90
LBB0_845:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
	incq	(%rbx)
LBB0_829:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_845
	jmp	LBB0_830
	.p2align	4, 0x90
LBB0_368:
	addq	$9, (%rbx)
	jmp	LBB0_369
	.p2align	4, 0x90
LBB0_846:
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 3(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	addq	$4, (%rbx)
LBB0_369:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_846
	.p2align	4, 0x90
LBB0_370:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_370
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 3(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_372
	.p2align	4, 0x90
LBB0_851:
	addq	$8, (%rbx)
LBB0_372:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_373
	addq	$7, (%rbx)
	jmp	LBB0_848
	.p2align	4, 0x90
LBB0_1416:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-6(%rax)
	addq	$6, (%rbx)
LBB0_848:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1416
	addq	$-6, (%rbx)
	jmp	LBB0_850
	.p2align	4, 0x90
LBB0_852:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	6(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	addq	$-2, (%rbx)
LBB0_850:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_852
	jmp	LBB0_851
	.p2align	4, 0x90
LBB0_373:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_373
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	incq	(%rbx)
	jmp	LBB0_375
	.p2align	4, 0x90
LBB0_853:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	addq	$5, (%rbx)
LBB0_375:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_853
	jmp	LBB0_376
	.p2align	4, 0x90
LBB0_857:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_376:
	addq	$2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_377
	movq	(%rbx), %rax
	decb	(%rax)
	addq	$-7, (%rbx)
	jmp	LBB0_855
	.p2align	4, 0x90
LBB0_1417:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$2, -1(%rax)
	addq	$-4, (%rbx)
LBB0_855:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1417
	jmp	LBB0_856
	.p2align	4, 0x90
LBB0_858:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-5(%rax)
LBB0_856:
	addq	$5, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_858
	jmp	LBB0_857
	.p2align	4, 0x90
LBB0_859:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
LBB0_377:
	addq	$-2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_859
	jmp	LBB0_378
	.p2align	4, 0x90
LBB0_860:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
LBB0_378:
	addq	$-5, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_860
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_380
	.p2align	4, 0x90
LBB0_861:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-4(%rax)
LBB0_380:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_861
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_382
	.p2align	4, 0x90
LBB0_871:
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 4(%rax)
LBB0_382:
	addq	$-4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_383
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	4(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_863
	.p2align	4, 0x90
LBB0_882:
	addq	$8, (%rbx)
LBB0_863:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_873
	jmp	LBB0_864
	.p2align	4, 0x90
LBB0_872:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-3(%rax)
LBB0_873:
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_872
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-3, (%rbx)
	.p2align	4, 0x90
LBB0_875:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_876
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	decq	(%rbx)
	jmp	LBB0_884
	.p2align	4, 0x90
LBB0_1418:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	addq	$2, (%rbx)
LBB0_884:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1418
	addq	$-2, (%rbx)
	jmp	LBB0_886
	.p2align	4, 0x90
LBB0_891:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	decq	(%rbx)
LBB0_886:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_875
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	addq	$-11, (%rbx)
	jmp	LBB0_888
	.p2align	4, 0x90
LBB0_1419:
	addq	$-9, (%rbx)
LBB0_888:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1419
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 4(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_890
	.p2align	4, 0x90
LBB0_892:
	addq	$9, (%rbx)
LBB0_890:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_892
	jmp	LBB0_891
	.p2align	4, 0x90
LBB0_876:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_877
	.p2align	4, 0x90
LBB0_893:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-2(%rax)
LBB0_877:
	addq	$2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_893
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-2, (%rbx)
	.p2align	4, 0x90
LBB0_879:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_880
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	2(%rax)
	incq	(%rbx)
	jmp	LBB0_895
	.p2align	4, 0x90
LBB0_1420:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	addq	$3, (%rbx)
LBB0_895:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1420
	addq	$-3, (%rbx)
	jmp	LBB0_897
	.p2align	4, 0x90
LBB0_902:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	decq	(%rbx)
LBB0_897:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_879
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$-12, (%rbx)
	jmp	LBB0_899
	.p2align	4, 0x90
LBB0_1421:
	addq	$-9, (%rbx)
LBB0_899:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1421
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 3(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$6, (%rbx)
	jmp	LBB0_901
	.p2align	4, 0x90
LBB0_903:
	addq	$9, (%rbx)
LBB0_901:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_903
	jmp	LBB0_902
	.p2align	4, 0x90
LBB0_880:
	movq	(%rbx), %rax
	incb	(%rax)
	incq	(%rbx)
	jmp	LBB0_881
	.p2align	4, 0x90
LBB0_906:
	addq	$-8, (%rbx)
LBB0_881:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_882
	movq	(%rbx), %rax
	decb	(%rax)
	decq	(%rbx)
	jmp	LBB0_905
	.p2align	4, 0x90
LBB0_907:
	addq	$9, (%rbx)
LBB0_905:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_907
	jmp	LBB0_906
	.p2align	4, 0x90
LBB0_864:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_864
	jmp	LBB0_865
	.p2align	4, 0x90
LBB0_908:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
LBB0_865:
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_908
	addq	$-3, (%rbx)
	jmp	LBB0_867
	.p2align	4, 0x90
LBB0_909:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$6, (%rbx)
	jmp	LBB0_910
	.p2align	4, 0x90
LBB0_921:
	addq	$8, (%rbx)
LBB0_910:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_911
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	jmp	LBB0_919
	.p2align	4, 0x90
LBB0_1422:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
LBB0_919:
	incq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1422
	jmp	LBB0_920
	.p2align	4, 0x90
LBB0_922:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_920:
	decq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_922
	jmp	LBB0_921
	.p2align	4, 0x90
LBB0_911:
	movq	(%rbx), %rax
	leaq	-8(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-8(%rax)
	decq	(%rbx)
	jmp	LBB0_912
	.p2align	4, 0x90
LBB0_929:
	addq	$-11, (%rbx)
LBB0_912:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_913
	incq	(%rbx)
	jmp	LBB0_924
	.p2align	4, 0x90
LBB0_934:
	decq	(%rbx)
LBB0_924:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_925
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$-2, (%rbx)
	jmp	LBB0_931
	.p2align	4, 0x90
LBB0_937:
	incq	(%rbx)
LBB0_931:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_932
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	2(%rax)
	movq	(%rbx), %rax
	leaq	-13(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-13(%rax)
	addq	$10, (%rbx)
	jmp	LBB0_936
	.p2align	4, 0x90
LBB0_938:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$-3, (%rbx)
LBB0_936:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_938
	jmp	LBB0_937
	.p2align	4, 0x90
LBB0_932:
	decq	(%rbx)
	jmp	LBB0_933
	.p2align	4, 0x90
LBB0_939:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	movq	(%rbx), %rax
	leaq	-13(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-13(%rax)
	addq	$10, (%rbx)
LBB0_933:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_939
	jmp	LBB0_934
	.p2align	4, 0x90
LBB0_925:
	addq	$2, (%rbx)
	jmp	LBB0_926
	.p2align	4, 0x90
LBB0_942:
	incq	(%rbx)
LBB0_926:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_927
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	addq	$-3, (%rbx)
	jmp	LBB0_941
	.p2align	4, 0x90
LBB0_943:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	movq	(%rbx), %rax
	leaq	-13(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-13(%rax)
	addq	$10, (%rbx)
LBB0_941:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_943
	jmp	LBB0_942
	.p2align	4, 0x90
LBB0_927:
	decq	(%rbx)
	jmp	LBB0_928
	.p2align	4, 0x90
LBB0_944:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$-3, (%rbx)
LBB0_928:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_944
	jmp	LBB0_929
	.p2align	4, 0x90
LBB0_913:
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 5(%rax)
	addq	$2, (%rbx)
	jmp	LBB0_914
	.p2align	4, 0x90
LBB0_945:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-7(%rax)
	addq	$7, (%rbx)
LBB0_914:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_945
	addq	$-7, (%rbx)
	jmp	LBB0_916
	.p2align	4, 0x90
LBB0_917:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	7(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	addq	$-5, (%rbx)
LBB0_916:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_917
LBB0_867:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_909
	jmp	LBB0_868
	.p2align	4, 0x90
LBB0_946:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
LBB0_868:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_946
	addq	$-4, (%rbx)
	.p2align	4, 0x90
LBB0_870:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_871
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_948
	.p2align	4, 0x90
LBB0_961:
	addq	$8, (%rbx)
LBB0_948:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_949
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	jmp	LBB0_959
	.p2align	4, 0x90
LBB0_1423:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-2(%rax)
LBB0_959:
	addq	$2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1423
	jmp	LBB0_960
	.p2align	4, 0x90
LBB0_962:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
LBB0_960:
	addq	$-2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_962
	jmp	LBB0_961
	.p2align	4, 0x90
LBB0_949:
	movq	(%rbx), %rax
	leaq	-8(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-8(%rax)
	decq	(%rbx)
	jmp	LBB0_950
	.p2align	4, 0x90
LBB0_957:
	addq	$-12, (%rbx)
LBB0_950:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_870
	incq	(%rbx)
	jmp	LBB0_952
	.p2align	4, 0x90
LBB0_967:
	addq	$-2, (%rbx)
LBB0_952:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_953
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$-3, (%rbx)
	jmp	LBB0_964
	.p2align	4, 0x90
LBB0_970:
	decq	(%rbx)
LBB0_964:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_965
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	movq	(%rbx), %rax
	leaq	-13(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-13(%rax)
	addq	$11, (%rbx)
	jmp	LBB0_969
	.p2align	4, 0x90
LBB0_971:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	addq	$-2, (%rbx)
LBB0_969:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_971
	jmp	LBB0_970
	.p2align	4, 0x90
LBB0_965:
	incq	(%rbx)
	jmp	LBB0_966
	.p2align	4, 0x90
LBB0_972:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	2(%rax)
	movq	(%rbx), %rax
	leaq	-13(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-13(%rax)
	addq	$11, (%rbx)
LBB0_966:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_972
	jmp	LBB0_967
	.p2align	4, 0x90
LBB0_953:
	incq	(%rbx)
	jmp	LBB0_954
	.p2align	4, 0x90
LBB0_975:
	decq	(%rbx)
LBB0_954:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_955
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$-2, (%rbx)
	jmp	LBB0_974
	.p2align	4, 0x90
LBB0_976:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	2(%rax)
	movq	(%rbx), %rax
	leaq	-13(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-13(%rax)
	addq	$11, (%rbx)
LBB0_974:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_976
	jmp	LBB0_975
	.p2align	4, 0x90
LBB0_955:
	incq	(%rbx)
	jmp	LBB0_956
	.p2align	4, 0x90
LBB0_977:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	addq	$-2, (%rbx)
LBB0_956:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_977
	jmp	LBB0_957
	.p2align	4, 0x90
LBB0_978:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
LBB0_383:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_978
	addq	$-4, (%rbx)
	.p2align	4, 0x90
LBB0_385:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_386
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	addq	$2, (%rbx)
	jmp	LBB0_980
	.p2align	4, 0x90
LBB0_1424:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-7(%rax)
	addq	$7, (%rbx)
LBB0_980:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1424
	addq	$-7, (%rbx)
	jmp	LBB0_982
	.p2align	4, 0x90
LBB0_1425:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	7(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	addq	$-5, (%rbx)
LBB0_982:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1425
	.p2align	4, 0x90
LBB0_983:
	addq	$9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_983
	addq	$-9, (%rbx)
	jmp	LBB0_985
	.p2align	4, 0x90
LBB0_992:
	addq	$-12, (%rbx)
LBB0_985:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_385
	incq	(%rbx)
	jmp	LBB0_987
	.p2align	4, 0x90
LBB0_997:
	addq	$-2, (%rbx)
LBB0_987:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_988
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$-3, (%rbx)
	jmp	LBB0_994
	.p2align	4, 0x90
LBB0_1000:
	decq	(%rbx)
LBB0_994:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_995
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	movq	(%rbx), %rax
	leaq	-13(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-13(%rax)
	addq	$11, (%rbx)
	jmp	LBB0_999
	.p2align	4, 0x90
LBB0_1001:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	addq	$-2, (%rbx)
LBB0_999:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1001
	jmp	LBB0_1000
	.p2align	4, 0x90
LBB0_995:
	incq	(%rbx)
	jmp	LBB0_996
	.p2align	4, 0x90
LBB0_1002:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	2(%rax)
	movq	(%rbx), %rax
	leaq	-13(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-13(%rax)
	addq	$11, (%rbx)
LBB0_996:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1002
	jmp	LBB0_997
	.p2align	4, 0x90
LBB0_988:
	incq	(%rbx)
	jmp	LBB0_989
	.p2align	4, 0x90
LBB0_1005:
	decq	(%rbx)
LBB0_989:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_990
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$-2, (%rbx)
	jmp	LBB0_1004
	.p2align	4, 0x90
LBB0_1006:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	2(%rax)
	movq	(%rbx), %rax
	leaq	-13(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-13(%rax)
	addq	$11, (%rbx)
LBB0_1004:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1006
	jmp	LBB0_1005
	.p2align	4, 0x90
LBB0_990:
	incq	(%rbx)
	jmp	LBB0_991
	.p2align	4, 0x90
LBB0_1007:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	addq	$-2, (%rbx)
LBB0_991:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1007
	jmp	LBB0_992
	.p2align	4, 0x90
LBB0_386:
	addq	$9, (%rbx)
	jmp	LBB0_387
	.p2align	4, 0x90
LBB0_1008:
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 2(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	addq	$6, (%rbx)
LBB0_387:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1008
	.p2align	4, 0x90
LBB0_388:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_388
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 3(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_390
	.p2align	4, 0x90
LBB0_1013:
	addq	$8, (%rbx)
LBB0_390:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_391
	addq	$5, (%rbx)
	jmp	LBB0_1010
	.p2align	4, 0x90
LBB0_1426:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	addq	$4, (%rbx)
LBB0_1010:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1426
	addq	$-4, (%rbx)
	jmp	LBB0_1012
	.p2align	4, 0x90
LBB0_1014:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	decq	(%rbx)
LBB0_1012:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1014
	jmp	LBB0_1013
	.p2align	4, 0x90
LBB0_391:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_391
	addq	$9, (%rbx)
	jmp	LBB0_393
	.p2align	4, 0x90
LBB0_1019:
	addq	$8, (%rbx)
LBB0_393:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_394
	addq	$6, (%rbx)
	jmp	LBB0_1016
	.p2align	4, 0x90
LBB0_1427:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-5(%rax)
	addq	$5, (%rbx)
LBB0_1016:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1427
	addq	$-5, (%rbx)
	jmp	LBB0_1018
	.p2align	4, 0x90
LBB0_1020:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	addq	$-2, (%rbx)
LBB0_1018:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1020
	jmp	LBB0_1019
	.p2align	4, 0x90
LBB0_394:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_394
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$15, 9(%rax)
	jmp	LBB0_396
	.p2align	4, 0x90
LBB0_1025:
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	9(%rax)
LBB0_396:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1022
	jmp	LBB0_397
	.p2align	4, 0x90
LBB0_1021:
	addq	$9, (%rbx)
LBB0_1022:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1021
	movq	(%rbx), %rax
	incb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	.p2align	4, 0x90
LBB0_1024:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1024
	jmp	LBB0_1025
	.p2align	4, 0x90
LBB0_397:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_398
	.p2align	4, 0x90
LBB0_1026:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	addq	$8, (%rbx)
LBB0_398:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1026
	.p2align	4, 0x90
LBB0_399:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_399
	addq	$9, (%rbx)
	jmp	LBB0_401
	.p2align	4, 0x90
LBB0_1036:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
	addq	$8, (%rbx)
LBB0_401:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_402
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	jmp	LBB0_1028
	.p2align	4, 0x90
LBB0_1428:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
LBB0_1028:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1428
	addq	$-4, (%rbx)
	jmp	LBB0_1030
	.p2align	4, 0x90
LBB0_1037:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$-5, (%rbx)
	jmp	LBB0_1038
	.p2align	4, 0x90
LBB0_1046:
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$9, (%rbx)
LBB0_1038:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1039
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_1043
	.p2align	4, 0x90
LBB0_1429:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
LBB0_1043:
	addq	$2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1429
	addq	$-2, (%rbx)
	jmp	LBB0_1045
	.p2align	4, 0x90
LBB0_1047:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	addq	$-4, (%rbx)
LBB0_1045:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1047
	jmp	LBB0_1046
	.p2align	4, 0x90
LBB0_1039:
	addq	$-8, (%rbx)
	jmp	LBB0_1040
	.p2align	4, 0x90
LBB0_1041:
	addq	$-9, (%rbx)
LBB0_1040:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1041
LBB0_1030:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1037
	.p2align	4, 0x90
LBB0_1031:
	addq	$9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1031
	addq	$-9, (%rbx)
	jmp	LBB0_1033
	.p2align	4, 0x90
LBB0_1050:
	addq	$-10, (%rbx)
LBB0_1033:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1034
	incq	(%rbx)
	jmp	LBB0_1049
	.p2align	4, 0x90
LBB0_1051:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_1049:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1051
	jmp	LBB0_1050
	.p2align	4, 0x90
LBB0_1034:
	incq	(%rbx)
	jmp	LBB0_1035
	.p2align	4, 0x90
LBB0_1052:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_1035:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1052
	jmp	LBB0_1036
	.p2align	4, 0x90
LBB0_1056:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
LBB0_402:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_403
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	jmp	LBB0_1054
	.p2align	4, 0x90
LBB0_1057:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	incq	(%rbx)
	jmp	LBB0_1058
	.p2align	4, 0x90
LBB0_1430:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-6(%rax)
	addq	$6, (%rbx)
LBB0_1058:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1430
	jmp	LBB0_1059
	.p2align	4, 0x90
LBB0_1060:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_1059:
	decq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1060
LBB0_1054:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1057
	jmp	LBB0_1055
	.p2align	4, 0x90
LBB0_1061:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
LBB0_1055:
	addq	$-3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1061
	jmp	LBB0_1056
	.p2align	4, 0x90
LBB0_403:
	addq	$9, (%rbx)
	jmp	LBB0_404
	.p2align	4, 0x90
LBB0_1062:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	addq	$8, (%rbx)
LBB0_404:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1062
	.p2align	4, 0x90
LBB0_405:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_405
	addq	$9, (%rbx)
	jmp	LBB0_407
	.p2align	4, 0x90
LBB0_1072:
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	addq	$8, (%rbx)
LBB0_407:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_408
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	jmp	LBB0_1064
	.p2align	4, 0x90
LBB0_1431:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-5(%rax)
LBB0_1064:
	addq	$5, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1431
	addq	$-5, (%rbx)
	jmp	LBB0_1066
	.p2align	4, 0x90
LBB0_1073:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	addq	$-6, (%rbx)
	jmp	LBB0_1074
	.p2align	4, 0x90
LBB0_1082:
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$9, (%rbx)
LBB0_1074:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1075
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_1079
	.p2align	4, 0x90
LBB0_1432:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
LBB0_1079:
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1432
	addq	$-3, (%rbx)
	jmp	LBB0_1081
	.p2align	4, 0x90
LBB0_1083:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	addq	$-4, (%rbx)
LBB0_1081:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1083
	jmp	LBB0_1082
	.p2align	4, 0x90
LBB0_1075:
	addq	$-8, (%rbx)
	jmp	LBB0_1076
	.p2align	4, 0x90
LBB0_1077:
	addq	$-9, (%rbx)
LBB0_1076:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1077
LBB0_1066:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1073
	.p2align	4, 0x90
LBB0_1067:
	addq	$9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1067
	addq	$-9, (%rbx)
	jmp	LBB0_1069
	.p2align	4, 0x90
LBB0_1086:
	addq	$-11, (%rbx)
LBB0_1069:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1070
	addq	$2, (%rbx)
	jmp	LBB0_1085
	.p2align	4, 0x90
LBB0_1087:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_1085:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1087
	jmp	LBB0_1086
	.p2align	4, 0x90
LBB0_1070:
	addq	$2, (%rbx)
	jmp	LBB0_1071
	.p2align	4, 0x90
LBB0_1088:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_1071:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1088
	jmp	LBB0_1072
	.p2align	4, 0x90
LBB0_1092:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
LBB0_408:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_409
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	jmp	LBB0_1090
	.p2align	4, 0x90
LBB0_1093:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	incq	(%rbx)
	jmp	LBB0_1094
	.p2align	4, 0x90
LBB0_1433:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-6(%rax)
	addq	$6, (%rbx)
LBB0_1094:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1433
	jmp	LBB0_1095
	.p2align	4, 0x90
LBB0_1096:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_1095:
	decq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1096
LBB0_1090:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1093
	jmp	LBB0_1091
	.p2align	4, 0x90
LBB0_1097:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
LBB0_1091:
	addq	$-3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1097
	jmp	LBB0_1092
	.p2align	4, 0x90
LBB0_409:
	addq	$9, (%rbx)
	jmp	LBB0_410
	.p2align	4, 0x90
LBB0_1100:
	addq	$5, (%rbx)
LBB0_410:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_411
	addq	$4, (%rbx)
	jmp	LBB0_1099
	.p2align	4, 0x90
LBB0_1101:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-36(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-36(%rax)
	addq	$36, (%rbx)
LBB0_1099:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1101
	jmp	LBB0_1100
	.p2align	4, 0x90
LBB0_411:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_411
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$15, 9(%rax)
	jmp	LBB0_413
	.p2align	4, 0x90
LBB0_1106:
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	9(%rax)
LBB0_413:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1103
	jmp	LBB0_414
	.p2align	4, 0x90
LBB0_1102:
	addq	$9, (%rbx)
LBB0_1103:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1102
	movq	(%rbx), %rax
	leaq	-9(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-9(%rax)
	.p2align	4, 0x90
LBB0_1105:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1105
	jmp	LBB0_1106
	.p2align	4, 0x90
LBB0_414:
	movq	(%rbx), %rax
	incb	(%rax)
	movq	(%rbx), %rax
	leaq	21(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	21(%rax)
	addq	$-3, (%rbx)
	jmp	LBB0_415
	.p2align	4, 0x90
LBB0_1107:
	addq	$-9, (%rbx)
LBB0_415:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1107
	addq	$9, (%rbx)
	jmp	LBB0_417
	.p2align	4, 0x90
LBB0_1118:
	addq	$8, (%rbx)
LBB0_417:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1109
	jmp	LBB0_418
	.p2align	4, 0x90
LBB0_1108:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-3(%rax)
LBB0_1109:
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1108
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-3, (%rbx)
	.p2align	4, 0x90
LBB0_1111:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1112
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	3(%rax)
	incq	(%rbx)
	jmp	LBB0_1120
	.p2align	4, 0x90
LBB0_1434:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	addq	$4, (%rbx)
LBB0_1120:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1434
	addq	$-4, (%rbx)
	jmp	LBB0_1122
	.p2align	4, 0x90
LBB0_1127:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	decq	(%rbx)
LBB0_1122:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1111
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$-13, (%rbx)
	jmp	LBB0_1124
	.p2align	4, 0x90
LBB0_1435:
	addq	$-9, (%rbx)
LBB0_1124:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1435
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 4(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_1126
	.p2align	4, 0x90
LBB0_1128:
	addq	$9, (%rbx)
LBB0_1126:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1128
	jmp	LBB0_1127
	.p2align	4, 0x90
LBB0_1112:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_1113
	.p2align	4, 0x90
LBB0_1129:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-4(%rax)
LBB0_1113:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1129
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-4, (%rbx)
	.p2align	4, 0x90
LBB0_1115:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1116
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	4(%rax)
	decq	(%rbx)
	jmp	LBB0_1131
	.p2align	4, 0x90
LBB0_1436:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	addq	$3, (%rbx)
LBB0_1131:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1436
	addq	$-3, (%rbx)
	jmp	LBB0_1133
	.p2align	4, 0x90
LBB0_1138:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	decq	(%rbx)
LBB0_1133:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1115
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	3(%rax)
	addq	$-12, (%rbx)
	jmp	LBB0_1135
	.p2align	4, 0x90
LBB0_1437:
	addq	$-9, (%rbx)
LBB0_1135:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1437
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 3(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$6, (%rbx)
	jmp	LBB0_1137
	.p2align	4, 0x90
LBB0_1139:
	addq	$9, (%rbx)
LBB0_1137:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1139
	jmp	LBB0_1138
	.p2align	4, 0x90
LBB0_1116:
	movq	(%rbx), %rax
	incb	(%rax)
	incq	(%rbx)
	jmp	LBB0_1117
	.p2align	4, 0x90
LBB0_1142:
	addq	$-8, (%rbx)
LBB0_1117:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1118
	movq	(%rbx), %rax
	decb	(%rax)
	decq	(%rbx)
	jmp	LBB0_1141
	.p2align	4, 0x90
LBB0_1143:
	addq	$9, (%rbx)
LBB0_1141:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1143
	jmp	LBB0_1142
	.p2align	4, 0x90
LBB0_418:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_418
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	2(%rax)
	addq	$2, (%rbx)
	jmp	LBB0_420
	.p2align	4, 0x90
LBB0_1144:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-4(%rax)
	addq	$4, (%rbx)
LBB0_420:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1144
	addq	$-4, (%rbx)
	jmp	LBB0_422
	.p2align	4, 0x90
LBB0_423:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, -2(%rax)
	addq	$-2, (%rbx)
LBB0_422:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_423
LBB0_102:
	addq	$2, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_284
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	jmp	LBB0_104
	.p2align	4, 0x90
LBB0_1145:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-4(%rax)
LBB0_104:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1145
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-4, (%rbx)
	jmp	LBB0_106
	.p2align	4, 0x90
LBB0_1146:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	4(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	movzbl	-6(%rax), %edi
	movl	$1, %esi
	callq	*%r14
	addq	$2, (%rbx)
LBB0_106:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1146
	addq	$4, (%rbx)
	jmp	LBB0_108
	.p2align	4, 0x90
LBB0_1147:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	movzbl	-7(%rax), %edi
	movl	$1, %esi
	callq	*%r14
	addq	$7, (%rbx)
LBB0_108:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1147
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, -3(%rax)
	jmp	LBB0_110
	.p2align	4, 0x90
LBB0_1148:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
LBB0_110:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1148
	.p2align	4, 0x90
LBB0_111:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_111
	addq	$9, (%rbx)
	jmp	LBB0_113
	.p2align	4, 0x90
LBB0_1149:
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 5(%rax)
	addq	$4, (%rbx)
LBB0_113:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1149
	.p2align	4, 0x90
LBB0_114:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_114
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$11, 1(%rax)
	jmp	LBB0_116
	.p2align	4, 0x90
LBB0_1152:
	addq	$9, (%rbx)
LBB0_116:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_117
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_1151
	.p2align	4, 0x90
LBB0_1153:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_1151:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1153
	jmp	LBB0_1152
	.p2align	4, 0x90
LBB0_117:
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-14, (%rbx)
	jmp	LBB0_118
	.p2align	4, 0x90
LBB0_1154:
	addq	$-9, (%rbx)
LBB0_118:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1154
	jmp	LBB0_119
	.p2align	4, 0x90
LBB0_1155:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-7(%rax)
LBB0_119:
	addq	$7, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1155
	addq	$-7, (%rbx)
	.p2align	4, 0x90
LBB0_121:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_122
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	7(%rax)
	movq	(%rbx), %rax
	movb	$0, (%rax)
	addq	$2, (%rbx)
	jmp	LBB0_1157
	.p2align	4, 0x90
LBB0_1438:
	addq	$9, (%rbx)
LBB0_1157:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1438
	addq	$-9, (%rbx)
	jmp	LBB0_1159
	.p2align	4, 0x90
LBB0_1164:
	addq	$-10, (%rbx)
LBB0_1159:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_121
	addq	$7, (%rbx)
	jmp	LBB0_1161
	.p2align	4, 0x90
LBB0_1439:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-6(%rax)
	addq	$6, (%rbx)
LBB0_1161:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1439
	addq	$-6, (%rbx)
	jmp	LBB0_1163
	.p2align	4, 0x90
LBB0_1167:
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 7(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$3, (%rbx)
LBB0_1163:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1164
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	6(%rax)
	addq	$-7, (%rbx)
	jmp	LBB0_1166
	.p2align	4, 0x90
LBB0_1168:
	addq	$-9, (%rbx)
LBB0_1166:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1168
	jmp	LBB0_1167
	.p2align	4, 0x90
LBB0_1169:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-7(%rax)
LBB0_122:
	addq	$7, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1169
	addq	$-7, (%rbx)
	jmp	LBB0_124
	.p2align	4, 0x90
LBB0_1176:
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	7(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, -4(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-3, (%rbx)
LBB0_124:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_125
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	7(%rax)
	addq	$2, (%rbx)
	jmp	LBB0_1171
	.p2align	4, 0x90
LBB0_1180:
	addq	$8, (%rbx)
LBB0_1171:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1172
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	jmp	LBB0_1178
	.p2align	4, 0x90
LBB0_1440:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-4(%rax)
LBB0_1178:
	addq	$4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1440
	jmp	LBB0_1179
	.p2align	4, 0x90
LBB0_1181:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
LBB0_1179:
	addq	$-4, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1181
	jmp	LBB0_1180
	.p2align	4, 0x90
LBB0_1172:
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	addq	$-7, (%rbx)
	jmp	LBB0_1173
	.p2align	4, 0x90
LBB0_1184:
	addq	$-14, (%rbx)
LBB0_1173:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1174
	addq	$5, (%rbx)
	jmp	LBB0_1183
	.p2align	4, 0x90
LBB0_1185:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	addq	$-2, (%rbx)
LBB0_1183:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1185
	jmp	LBB0_1184
	.p2align	4, 0x90
LBB0_1174:
	addq	$9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1174
	jmp	LBB0_1175
	.p2align	4, 0x90
LBB0_1189:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
LBB0_1175:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1176
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	jmp	LBB0_1187
	.p2align	4, 0x90
LBB0_1190:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-7(%rax)
	incq	(%rbx)
	jmp	LBB0_1191
	.p2align	4, 0x90
LBB0_1441:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	addq	$3, (%rbx)
LBB0_1191:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1441
	jmp	LBB0_1192
	.p2align	4, 0x90
LBB0_1193:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_1192:
	decq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1193
LBB0_1187:
	addq	$7, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1190
	jmp	LBB0_1188
	.p2align	4, 0x90
LBB0_1194:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	6(%rax)
LBB0_1188:
	addq	$-6, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1194
	jmp	LBB0_1189
	.p2align	4, 0x90
LBB0_125:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_126
	.p2align	4, 0x90
LBB0_1195:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-7(%rax)
LBB0_126:
	addq	$7, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1195
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-7, (%rbx)
	jmp	LBB0_128
	.p2align	4, 0x90
LBB0_129:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	7(%rax)
	addq	$2, (%rbx)
	jmp	LBB0_130
	.p2align	4, 0x90
LBB0_1198:
	addq	$4, (%rbx)
LBB0_130:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_131
	addq	$5, (%rbx)
	jmp	LBB0_1197
	.p2align	4, 0x90
LBB0_1199:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	addq	$-2, (%rbx)
LBB0_1197:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1199
	jmp	LBB0_1198
	.p2align	4, 0x90
LBB0_1203:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
LBB0_131:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_132
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	jmp	LBB0_1201
	.p2align	4, 0x90
LBB0_1204:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-7(%rax)
	incq	(%rbx)
	jmp	LBB0_1205
	.p2align	4, 0x90
LBB0_1442:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-3(%rax)
	addq	$3, (%rbx)
LBB0_1205:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1442
	jmp	LBB0_1206
	.p2align	4, 0x90
LBB0_1207:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_1206:
	decq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1207
LBB0_1201:
	addq	$7, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1204
	jmp	LBB0_1202
	.p2align	4, 0x90
LBB0_1208:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	6(%rax)
LBB0_1202:
	addq	$-6, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1208
	jmp	LBB0_1203
	.p2align	4, 0x90
LBB0_132:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$5, 1(%rax)
	jmp	LBB0_133
	.p2align	4, 0x90
LBB0_1211:
	addq	$9, (%rbx)
LBB0_133:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_134
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_1210
	.p2align	4, 0x90
LBB0_1212:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_1210:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1212
	jmp	LBB0_1211
	.p2align	4, 0x90
LBB0_134:
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	4(%rax)
	addq	$-5, (%rbx)
	jmp	LBB0_135
	.p2align	4, 0x90
LBB0_1213:
	addq	$-9, (%rbx)
LBB0_135:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1213
	addq	$9, (%rbx)
	jmp	LBB0_137
	.p2align	4, 0x90
LBB0_1224:
	addq	$8, (%rbx)
LBB0_137:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1215
	jmp	LBB0_138
	.p2align	4, 0x90
LBB0_1214:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-5(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-5(%rax)
LBB0_1215:
	addq	$5, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1214
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-5, (%rbx)
	.p2align	4, 0x90
LBB0_1217:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1218
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	5(%rax)
	addq	$2, (%rbx)
	jmp	LBB0_1226
	.p2align	4, 0x90
LBB0_1443:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-7(%rax)
	addq	$7, (%rbx)
LBB0_1226:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1443
	addq	$-7, (%rbx)
	jmp	LBB0_1228
	.p2align	4, 0x90
LBB0_1233:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	decq	(%rbx)
LBB0_1228:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1217
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	7(%rax)
	addq	$-16, (%rbx)
	jmp	LBB0_1230
	.p2align	4, 0x90
LBB0_1444:
	addq	$-9, (%rbx)
LBB0_1230:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1444
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 4(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_1232
	.p2align	4, 0x90
LBB0_1234:
	addq	$9, (%rbx)
LBB0_1232:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1234
	jmp	LBB0_1233
	.p2align	4, 0x90
LBB0_1218:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_1219
	.p2align	4, 0x90
LBB0_1235:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-7(%rax)
LBB0_1219:
	addq	$7, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1235
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-7, (%rbx)
	.p2align	4, 0x90
LBB0_1221:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1222
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	7(%rax)
	addq	$-2, (%rbx)
	jmp	LBB0_1237
	.p2align	4, 0x90
LBB0_1445:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-5(%rax)
	addq	$5, (%rbx)
LBB0_1237:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1445
	addq	$-5, (%rbx)
	jmp	LBB0_1239
	.p2align	4, 0x90
LBB0_1244:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	decq	(%rbx)
LBB0_1239:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1221
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	addq	$-14, (%rbx)
	jmp	LBB0_1241
	.p2align	4, 0x90
LBB0_1446:
	addq	$-9, (%rbx)
LBB0_1241:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1446
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 3(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$6, (%rbx)
	jmp	LBB0_1243
	.p2align	4, 0x90
LBB0_1245:
	addq	$9, (%rbx)
LBB0_1243:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1245
	jmp	LBB0_1244
	.p2align	4, 0x90
LBB0_1222:
	movq	(%rbx), %rax
	incb	(%rax)
	incq	(%rbx)
	jmp	LBB0_1223
	.p2align	4, 0x90
LBB0_1248:
	addq	$-8, (%rbx)
LBB0_1223:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1224
	movq	(%rbx), %rax
	decb	(%rax)
	decq	(%rbx)
	jmp	LBB0_1247
	.p2align	4, 0x90
LBB0_1249:
	addq	$9, (%rbx)
LBB0_1247:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1249
	jmp	LBB0_1248
	.p2align	4, 0x90
LBB0_138:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_138
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 4(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$5, -3(%rax)
	jmp	LBB0_140
	.p2align	4, 0x90
LBB0_1252:
	addq	$9, (%rbx)
LBB0_140:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_141
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_1251
	.p2align	4, 0x90
LBB0_1253:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_1251:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1253
	jmp	LBB0_1252
	.p2align	4, 0x90
LBB0_141:
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	4(%rax)
	addq	$-5, (%rbx)
	jmp	LBB0_142
	.p2align	4, 0x90
LBB0_143:
	addq	$-9, (%rbx)
LBB0_142:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_143
LBB0_128:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_129
LBB0_35:
	addq	$3, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_63
	movq	(%rbx), %rax
	leaq	-4(%rax), %rcx
	movq	%rcx, (%rbx)
	movzbl	-4(%rax), %edi
	movl	$1, %esi
	callq	*%r14
	addq	$10, (%rbx)
	jmp	LBB0_37
	.p2align	4, 0x90
LBB0_1254:
	movq	(%rbx), %rax
	leaq	6(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 6(%rax)
	addq	$3, (%rbx)
LBB0_37:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1254
	.p2align	4, 0x90
LBB0_38:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_38
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$10, 1(%rax)
	jmp	LBB0_40
	.p2align	4, 0x90
LBB0_1257:
	addq	$9, (%rbx)
LBB0_40:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_41
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_1256
	.p2align	4, 0x90
LBB0_1258:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_1256:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1258
	jmp	LBB0_1257
	.p2align	4, 0x90
LBB0_41:
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-15, (%rbx)
	jmp	LBB0_42
	.p2align	4, 0x90
LBB0_1259:
	addq	$-9, (%rbx)
LBB0_42:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1259
	jmp	LBB0_43
	.p2align	4, 0x90
LBB0_1260:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-8(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-8(%rax)
LBB0_43:
	addq	$8, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1260
	addq	$-8, (%rbx)
	.p2align	4, 0x90
LBB0_45:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_46
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	8(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	8(%rax)
	movq	(%rbx), %rax
	movb	$0, (%rax)
	incq	(%rbx)
	jmp	LBB0_1262
	.p2align	4, 0x90
LBB0_1447:
	addq	$9, (%rbx)
LBB0_1262:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1447
	addq	$-9, (%rbx)
	jmp	LBB0_1264
	.p2align	4, 0x90
LBB0_1269:
	addq	$-10, (%rbx)
LBB0_1264:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_45
	addq	$8, (%rbx)
	jmp	LBB0_1266
	.p2align	4, 0x90
LBB0_1448:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-7(%rax)
	addq	$7, (%rbx)
LBB0_1266:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1448
	addq	$-7, (%rbx)
	jmp	LBB0_1268
	.p2align	4, 0x90
LBB0_1272:
	movq	(%rbx), %rax
	leaq	8(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 8(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$2, (%rbx)
LBB0_1268:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1269
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	7(%rax)
	addq	$-8, (%rbx)
	jmp	LBB0_1271
	.p2align	4, 0x90
LBB0_1273:
	addq	$-9, (%rbx)
LBB0_1271:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1273
	jmp	LBB0_1272
	.p2align	4, 0x90
LBB0_1274:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-8(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-8(%rax)
LBB0_46:
	addq	$8, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1274
	addq	$-8, (%rbx)
	jmp	LBB0_48
	.p2align	4, 0x90
LBB0_1281:
	movq	(%rbx), %rax
	leaq	8(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	8(%rax)
	movq	(%rbx), %rax
	leaq	-5(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, -5(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-3, (%rbx)
LBB0_48:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_49
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	8(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	8(%rax)
	incq	(%rbx)
	jmp	LBB0_1276
	.p2align	4, 0x90
LBB0_1285:
	addq	$8, (%rbx)
LBB0_1276:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1277
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	jmp	LBB0_1283
	.p2align	4, 0x90
LBB0_1449:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-5(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-5(%rax)
LBB0_1283:
	addq	$5, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1449
	jmp	LBB0_1284
	.p2align	4, 0x90
LBB0_1286:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
LBB0_1284:
	addq	$-5, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1286
	jmp	LBB0_1285
	.p2align	4, 0x90
LBB0_1277:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
	addq	$-8, (%rbx)
	jmp	LBB0_1278
	.p2align	4, 0x90
LBB0_1289:
	addq	$-15, (%rbx)
LBB0_1278:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1279
	addq	$6, (%rbx)
	jmp	LBB0_1288
	.p2align	4, 0x90
LBB0_1290:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	addq	$-2, (%rbx)
LBB0_1288:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1290
	jmp	LBB0_1289
	.p2align	4, 0x90
LBB0_1279:
	addq	$9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1279
	jmp	LBB0_1280
	.p2align	4, 0x90
LBB0_1294:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
LBB0_1280:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1281
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	jmp	LBB0_1292
	.p2align	4, 0x90
LBB0_1295:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-8(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-8(%rax)
	incq	(%rbx)
	jmp	LBB0_1296
	.p2align	4, 0x90
LBB0_1450:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	addq	$2, (%rbx)
LBB0_1296:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1450
	jmp	LBB0_1297
	.p2align	4, 0x90
LBB0_1298:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_1297:
	decq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1298
LBB0_1292:
	addq	$8, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1295
	jmp	LBB0_1293
	.p2align	4, 0x90
LBB0_1299:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	7(%rax)
LBB0_1293:
	addq	$-7, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1299
	jmp	LBB0_1294
	.p2align	4, 0x90
LBB0_49:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_50
	.p2align	4, 0x90
LBB0_1300:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-8(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-8(%rax)
LBB0_50:
	addq	$8, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1300
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-8, (%rbx)
	jmp	LBB0_52
	.p2align	4, 0x90
LBB0_1301:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	8(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	8(%rax)
	incq	(%rbx)
	jmp	LBB0_1302
	.p2align	4, 0x90
LBB0_1318:
	addq	$3, (%rbx)
LBB0_1302:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1303
	addq	$6, (%rbx)
	jmp	LBB0_1317
	.p2align	4, 0x90
LBB0_1319:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	2(%rax)
	addq	$-2, (%rbx)
LBB0_1317:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1319
	jmp	LBB0_1318
	.p2align	4, 0x90
LBB0_1323:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-1(%rax)
LBB0_1303:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1304
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	jmp	LBB0_1321
	.p2align	4, 0x90
LBB0_1324:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-8(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-8(%rax)
	incq	(%rbx)
	jmp	LBB0_1325
	.p2align	4, 0x90
LBB0_1451:
	movq	(%rbx), %rax
	leaq	-1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-1(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	1(%rax)
	movq	(%rbx), %rax
	leaq	-2(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-2(%rax)
	addq	$2, (%rbx)
LBB0_1325:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1451
	jmp	LBB0_1326
	.p2align	4, 0x90
LBB0_1327:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
LBB0_1326:
	decq	(%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1327
LBB0_1321:
	addq	$8, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1324
	jmp	LBB0_1322
	.p2align	4, 0x90
LBB0_1328:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	7(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	7(%rax)
LBB0_1322:
	addq	$-7, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1328
	jmp	LBB0_1323
	.p2align	4, 0x90
LBB0_1304:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$5, 1(%rax)
	jmp	LBB0_1305
	.p2align	4, 0x90
LBB0_1331:
	addq	$9, (%rbx)
LBB0_1305:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1306
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_1330
	.p2align	4, 0x90
LBB0_1332:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_1330:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1332
	jmp	LBB0_1331
	.p2align	4, 0x90
LBB0_1306:
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	5(%rax)
	movq	(%rbx), %rax
	leaq	27(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	27(%rax)
	addq	$-6, (%rbx)
	jmp	LBB0_1307
	.p2align	4, 0x90
LBB0_1333:
	addq	$-9, (%rbx)
LBB0_1307:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1333
	addq	$9, (%rbx)
	jmp	LBB0_1309
	.p2align	4, 0x90
LBB0_1344:
	addq	$8, (%rbx)
LBB0_1309:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1335
	jmp	LBB0_1310
	.p2align	4, 0x90
LBB0_1334:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-6(%rax)
LBB0_1335:
	addq	$6, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1334
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-6, (%rbx)
	.p2align	4, 0x90
LBB0_1337:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1338
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	6(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	6(%rax)
	addq	$2, (%rbx)
	jmp	LBB0_1346
	.p2align	4, 0x90
LBB0_1452:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-8(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-8(%rax)
	addq	$8, (%rbx)
LBB0_1346:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1452
	addq	$-8, (%rbx)
	jmp	LBB0_1348
	.p2align	4, 0x90
LBB0_1353:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	1(%rax)
	decq	(%rbx)
LBB0_1348:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1337
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	8(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	8(%rax)
	addq	$-17, (%rbx)
	jmp	LBB0_1350
	.p2align	4, 0x90
LBB0_1453:
	addq	$-9, (%rbx)
LBB0_1350:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1453
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 4(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$5, (%rbx)
	jmp	LBB0_1352
	.p2align	4, 0x90
LBB0_1354:
	addq	$9, (%rbx)
LBB0_1352:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1354
	jmp	LBB0_1353
	.p2align	4, 0x90
LBB0_1338:
	movq	(%rbx), %rax
	incb	(%rax)
	jmp	LBB0_1339
	.p2align	4, 0x90
LBB0_1355:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-8(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	-8(%rax)
LBB0_1339:
	addq	$8, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1355
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$-8, (%rbx)
	.p2align	4, 0x90
LBB0_1341:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1342
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	8(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	8(%rax)
	addq	$-2, (%rbx)
	jmp	LBB0_1357
	.p2align	4, 0x90
LBB0_1454:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	-6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	-6(%rax)
	addq	$6, (%rbx)
LBB0_1357:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1454
	addq	$-6, (%rbx)
	jmp	LBB0_1359
	.p2align	4, 0x90
LBB0_1364:
	movq	(%rbx), %rax
	leaq	1(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 1(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	decq	(%rbx)
LBB0_1359:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1341
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	6(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	6(%rax)
	addq	$-15, (%rbx)
	jmp	LBB0_1361
	.p2align	4, 0x90
LBB0_1455:
	addq	$-9, (%rbx)
LBB0_1361:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1455
	movq	(%rbx), %rax
	leaq	3(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 3(%rax)
	movq	(%rbx), %rax
	incb	(%rax)
	addq	$6, (%rbx)
	jmp	LBB0_1363
	.p2align	4, 0x90
LBB0_1365:
	addq	$9, (%rbx)
LBB0_1363:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1365
	jmp	LBB0_1364
	.p2align	4, 0x90
LBB0_1342:
	movq	(%rbx), %rax
	incb	(%rax)
	incq	(%rbx)
	jmp	LBB0_1343
	.p2align	4, 0x90
LBB0_1368:
	addq	$-8, (%rbx)
LBB0_1343:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1344
	movq	(%rbx), %rax
	decb	(%rax)
	decq	(%rbx)
	jmp	LBB0_1367
	.p2align	4, 0x90
LBB0_1369:
	addq	$9, (%rbx)
LBB0_1367:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1369
	jmp	LBB0_1368
	.p2align	4, 0x90
LBB0_1310:
	addq	$-9, (%rbx)
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1310
	movq	(%rbx), %rax
	leaq	4(%rax), %rcx
	movq	%rcx, (%rbx)
	movb	$0, 4(%rax)
	movq	(%rbx), %rax
	leaq	-3(%rax), %rcx
	movq	%rcx, (%rbx)
	addb	$5, -3(%rax)
	jmp	LBB0_1312
	.p2align	4, 0x90
LBB0_1372:
	addq	$9, (%rbx)
LBB0_1312:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	je	LBB0_1313
	movq	(%rbx), %rax
	decb	(%rax)
	jmp	LBB0_1371
	.p2align	4, 0x90
LBB0_1373:
	movq	(%rbx), %rax
	decb	(%rax)
	movq	(%rbx), %rax
	leaq	9(%rax), %rcx
	movq	%rcx, (%rbx)
	incb	9(%rax)
	addq	$-9, (%rbx)
LBB0_1371:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1373
	jmp	LBB0_1372
	.p2align	4, 0x90
LBB0_1313:
	movq	(%rbx), %rax
	leaq	5(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	5(%rax)
	movq	(%rbx), %rax
	leaq	27(%rax), %rcx
	movq	%rcx, (%rbx)
	decb	27(%rax)
	addq	$-6, (%rbx)
	jmp	LBB0_1314
	.p2align	4, 0x90
LBB0_1315:
	addq	$-9, (%rbx)
LBB0_1314:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1315
LBB0_52:
	movq	(%rbx), %rax
	cmpb	$0, (%rax)
	jne	LBB0_1301
	jmp	LBB0_53
LBB0_13:
	xorl	%eax, %eax
	addq	$8, %rsp
	popq	%rbx
	popq	%r14
	retq
	.cfi_endproc

.zerofill __DATA,__bss,_ptr,8,3

.subsections_via_symbols
