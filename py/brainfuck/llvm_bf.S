	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 15
	.globl	_foo
	.p2align	4, 0x90
_foo:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	pushq	%r14
	.cfi_def_cfa_offset 24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset %rbx, -32
	.cfi_offset %r14, -24
	.cfi_offset %r15, -16
	movq	%rdi, %rbx
	movabsq	$_ptr, %r14
	movslq	(%r14), %rax
	addb	$13, (%rdi,%rax)
	jmp	LBB0_1
	.p2align	4, 0x90
LBB0_1374:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	addb	$2, (%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	addb	$5, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	addb	$2, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-6, (%r14)
LBB0_1:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1374
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	addb	$6, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	addb	$-3, (%rbx,%rax)
	movl	(%r14), %eax
	addl	$10, %eax
	movl	%eax, (%r14)
	cltq
	addb	$15, (%rbx,%rax)
	jmp	LBB0_3
	.p2align	4, 0x90
LBB0_18:
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_3:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_15
	jmp	LBB0_4
	.p2align	4, 0x90
LBB0_14:
	addl	$9, (%r14)
LBB0_15:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_14
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_17
	.p2align	4, 0x90
LBB0_19:
	addl	$-9, (%r14)
LBB0_17:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_19
	jmp	LBB0_18
LBB0_4:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_5
	.p2align	4, 0x90
LBB0_20:
	movl	(%r14), %eax
	addl	$8, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	incl	(%r14)
LBB0_5:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_20
	.p2align	4, 0x90
LBB0_6:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_6
	movl	(%r14), %eax
	addl	$8, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	addb	$5, (%rbx,%rax)
	jmp	LBB0_8
	.p2align	4, 0x90
LBB0_23:
	addl	$9, (%r14)
LBB0_8:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_9
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_22
	.p2align	4, 0x90
LBB0_24:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_22:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_24
	jmp	LBB0_23
LBB0_9:
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$27, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-17, (%r14)
	jmp	LBB0_10
	.p2align	4, 0x90
LBB0_25:
	addl	$-9, (%r14)
LBB0_10:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_25
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	movabsq	$_sys_write, %r15
	jmp	LBB0_12
	.p2align	4, 0x90
LBB0_53:
	addl	$3, (%r14)
LBB0_12:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_13
	addl	$6, (%r14)
	jmp	LBB0_27
	.p2align	4, 0x90
LBB0_1375:
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$2, (%r14)
LBB0_27:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1375
	.p2align	4, 0x90
LBB0_28:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_28
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	addb	$4, (%rbx,%rax)
	jmp	LBB0_30
	.p2align	4, 0x90
LBB0_56:
	addl	$9, (%r14)
LBB0_30:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_31
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_55
	.p2align	4, 0x90
LBB0_57:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_55:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_57
	jmp	LBB0_56
	.p2align	4, 0x90
LBB0_31:
	movl	(%r14), %eax
	addl	$6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	addb	$7, (%rbx,%rax)
	jmp	LBB0_32
	.p2align	4, 0x90
LBB0_60:
	addl	$9, (%r14)
LBB0_32:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_33
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_59
	.p2align	4, 0x90
LBB0_61:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_59:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_61
	jmp	LBB0_60
	.p2align	4, 0x90
LBB0_33:
	movl	(%r14), %eax
	addl	$6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-16, (%r14)
	jmp	LBB0_34
	.p2align	4, 0x90
LBB0_62:
	addl	$-9, (%r14)
LBB0_34:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_62
	jmp	LBB0_35
	.p2align	4, 0x90
LBB0_63:
	movslq	(%r14), %rax
	movb	$0, (%rbx,%rax)
	addl	$6, (%r14)
	jmp	LBB0_64
	.p2align	4, 0x90
LBB0_148:
	addl	$8, (%r14)
LBB0_64:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_65
	addl	$7, (%r14)
	jmp	LBB0_145
	.p2align	4, 0x90
LBB0_1376:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$6, (%r14)
LBB0_145:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1376
	addl	$-6, (%r14)
	jmp	LBB0_147
	.p2align	4, 0x90
LBB0_149:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_147:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_149
	jmp	LBB0_148
	.p2align	4, 0x90
LBB0_65:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_65
	addl	$9, (%r14)
	jmp	LBB0_67
	.p2align	4, 0x90
LBB0_154:
	addl	$8, (%r14)
LBB0_67:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_68
	addl	$8, (%r14)
	jmp	LBB0_151
	.p2align	4, 0x90
LBB0_1377:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$7, (%r14)
LBB0_151:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1377
	addl	$-7, (%r14)
	jmp	LBB0_153
	.p2align	4, 0x90
LBB0_155:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
LBB0_153:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_155
	jmp	LBB0_154
	.p2align	4, 0x90
LBB0_68:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_68
	jmp	LBB0_69
	.p2align	4, 0x90
LBB0_156:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_69:
	addl	$7, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_156
	addl	$-7, (%r14)
	jmp	LBB0_71
	.p2align	4, 0x90
LBB0_157:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-5, (%r14)
LBB0_71:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_157
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	addb	$15, (%rbx,%rax)
	jmp	LBB0_73
	.p2align	4, 0x90
LBB0_162:
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_73:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_159
	jmp	LBB0_74
	.p2align	4, 0x90
LBB0_158:
	addl	$9, (%r14)
LBB0_159:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_158
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	.p2align	4, 0x90
LBB0_161:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_161
	jmp	LBB0_162
	.p2align	4, 0x90
LBB0_74:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_75
	.p2align	4, 0x90
LBB0_163:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_75:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_163
	.p2align	4, 0x90
LBB0_76:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_76
	addl	$9, (%r14)
	jmp	LBB0_78
	.p2align	4, 0x90
LBB0_173:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_78:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_79
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_165
	.p2align	4, 0x90
LBB0_1378:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_165:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1378
	addl	$-4, (%r14)
	jmp	LBB0_167
	.p2align	4, 0x90
LBB0_174:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-5, (%r14)
	jmp	LBB0_175
	.p2align	4, 0x90
LBB0_183:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$9, (%r14)
LBB0_175:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_176
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_180
	.p2align	4, 0x90
LBB0_1379:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_180:
	addl	$2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1379
	addl	$-2, (%r14)
	jmp	LBB0_182
	.p2align	4, 0x90
LBB0_184:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
LBB0_182:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_184
	jmp	LBB0_183
	.p2align	4, 0x90
LBB0_176:
	addl	$-8, (%r14)
	jmp	LBB0_177
	.p2align	4, 0x90
LBB0_178:
	addl	$-9, (%r14)
LBB0_177:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_178
LBB0_167:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_174
	.p2align	4, 0x90
LBB0_168:
	addl	$9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_168
	addl	$-9, (%r14)
	jmp	LBB0_170
	.p2align	4, 0x90
LBB0_187:
	addl	$-10, (%r14)
LBB0_170:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_171
	incl	(%r14)
	jmp	LBB0_186
	.p2align	4, 0x90
LBB0_188:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_186:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_188
	jmp	LBB0_187
	.p2align	4, 0x90
LBB0_171:
	incl	(%r14)
	jmp	LBB0_172
	.p2align	4, 0x90
LBB0_189:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_172:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_189
	jmp	LBB0_173
	.p2align	4, 0x90
LBB0_193:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_79:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_80
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_191
	.p2align	4, 0x90
LBB0_194:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_195
	.p2align	4, 0x90
LBB0_1380:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$6, (%r14)
LBB0_195:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1380
	jmp	LBB0_196
	.p2align	4, 0x90
LBB0_197:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_196:
	decl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_197
LBB0_191:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_194
	jmp	LBB0_192
	.p2align	4, 0x90
LBB0_198:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_192:
	addl	$-3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_198
	jmp	LBB0_193
	.p2align	4, 0x90
LBB0_80:
	addl	$9, (%r14)
	jmp	LBB0_81
	.p2align	4, 0x90
LBB0_199:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_81:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_199
	.p2align	4, 0x90
LBB0_82:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_82
	addl	$9, (%r14)
	jmp	LBB0_84
	.p2align	4, 0x90
LBB0_209:
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_84:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_85
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_201
	.p2align	4, 0x90
LBB0_1381:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_201:
	addl	$5, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1381
	addl	$-5, (%r14)
	jmp	LBB0_203
	.p2align	4, 0x90
LBB0_210:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-6, (%r14)
	jmp	LBB0_211
	.p2align	4, 0x90
LBB0_219:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$9, (%r14)
LBB0_211:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_212
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_216
	.p2align	4, 0x90
LBB0_1382:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_216:
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1382
	addl	$-3, (%r14)
	jmp	LBB0_218
	.p2align	4, 0x90
LBB0_220:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
LBB0_218:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_220
	jmp	LBB0_219
	.p2align	4, 0x90
LBB0_212:
	addl	$-8, (%r14)
	jmp	LBB0_213
	.p2align	4, 0x90
LBB0_214:
	addl	$-9, (%r14)
LBB0_213:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_214
LBB0_203:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_210
	.p2align	4, 0x90
LBB0_204:
	addl	$9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_204
	addl	$-9, (%r14)
	jmp	LBB0_206
	.p2align	4, 0x90
LBB0_223:
	addl	$-11, (%r14)
LBB0_206:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_207
	addl	$2, (%r14)
	jmp	LBB0_222
	.p2align	4, 0x90
LBB0_224:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_222:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_224
	jmp	LBB0_223
	.p2align	4, 0x90
LBB0_207:
	addl	$2, (%r14)
	jmp	LBB0_208
	.p2align	4, 0x90
LBB0_225:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_208:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_225
	jmp	LBB0_209
	.p2align	4, 0x90
LBB0_229:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_85:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_86
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_227
	.p2align	4, 0x90
LBB0_230:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_231
	.p2align	4, 0x90
LBB0_1383:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$6, (%r14)
LBB0_231:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1383
	jmp	LBB0_232
	.p2align	4, 0x90
LBB0_233:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_232:
	decl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_233
LBB0_227:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_230
	jmp	LBB0_228
	.p2align	4, 0x90
LBB0_234:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_228:
	addl	$-3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_234
	jmp	LBB0_229
	.p2align	4, 0x90
LBB0_86:
	addl	$9, (%r14)
	jmp	LBB0_87
	.p2align	4, 0x90
LBB0_237:
	addl	$5, (%r14)
LBB0_87:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_88
	addl	$4, (%r14)
	jmp	LBB0_236
	.p2align	4, 0x90
LBB0_238:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-36, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$36, (%r14)
LBB0_236:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_238
	jmp	LBB0_237
	.p2align	4, 0x90
LBB0_88:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_88
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	addb	$15, (%rbx,%rax)
	jmp	LBB0_90
	.p2align	4, 0x90
LBB0_243:
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_90:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_240
	jmp	LBB0_91
	.p2align	4, 0x90
LBB0_239:
	addl	$9, (%r14)
LBB0_240:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_239
	movl	(%r14), %eax
	addl	$-9, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	.p2align	4, 0x90
LBB0_242:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_242
	jmp	LBB0_243
	.p2align	4, 0x90
LBB0_91:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$21, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
	jmp	LBB0_92
	.p2align	4, 0x90
LBB0_244:
	addl	$-9, (%r14)
LBB0_92:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_244
	addl	$9, (%r14)
	jmp	LBB0_94
	.p2align	4, 0x90
LBB0_255:
	addl	$8, (%r14)
LBB0_94:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_246
	jmp	LBB0_95
	.p2align	4, 0x90
LBB0_245:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_246:
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_245
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
	.p2align	4, 0x90
LBB0_248:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_249
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_257
	.p2align	4, 0x90
LBB0_1384:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$4, (%r14)
LBB0_257:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1384
	addl	$-4, (%r14)
	jmp	LBB0_259
	.p2align	4, 0x90
LBB0_264:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_259:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_248
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-13, (%r14)
	jmp	LBB0_261
	.p2align	4, 0x90
LBB0_1385:
	addl	$-9, (%r14)
LBB0_261:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1385
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_263
	.p2align	4, 0x90
LBB0_265:
	addl	$9, (%r14)
LBB0_263:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_265
	jmp	LBB0_264
	.p2align	4, 0x90
LBB0_249:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_250
	.p2align	4, 0x90
LBB0_266:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_250:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_266
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
	.p2align	4, 0x90
LBB0_252:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_253
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_268
	.p2align	4, 0x90
LBB0_1386:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$3, (%r14)
LBB0_268:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1386
	addl	$-3, (%r14)
	jmp	LBB0_270
	.p2align	4, 0x90
LBB0_275:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_270:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_252
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-12, (%r14)
	jmp	LBB0_272
	.p2align	4, 0x90
LBB0_1387:
	addl	$-9, (%r14)
LBB0_272:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1387
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$6, (%r14)
	jmp	LBB0_274
	.p2align	4, 0x90
LBB0_276:
	addl	$9, (%r14)
LBB0_274:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_276
	jmp	LBB0_275
	.p2align	4, 0x90
LBB0_253:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_254
	.p2align	4, 0x90
LBB0_279:
	addl	$-8, (%r14)
LBB0_254:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_255
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_278
	.p2align	4, 0x90
LBB0_280:
	addl	$9, (%r14)
LBB0_278:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_280
	jmp	LBB0_279
	.p2align	4, 0x90
LBB0_95:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_95
	addl	$-7, (%r14)
	jmp	LBB0_97
	.p2align	4, 0x90
LBB0_281:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	addl	$-4, (%r14)
LBB0_97:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_281
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	addb	$26, (%rbx,%rax)
	addl	$2, (%r14)
	jmp	LBB0_99
	.p2align	4, 0x90
LBB0_282:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$4, (%r14)
LBB0_99:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_282
	addl	$-4, (%r14)
	jmp	LBB0_101
	.p2align	4, 0x90
LBB0_283:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$-2, (%r14)
LBB0_101:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_283
	jmp	LBB0_102
	.p2align	4, 0x90
LBB0_284:
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_285
	.p2align	4, 0x90
LBB0_1388:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
LBB0_285:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1388
	incl	(%r14)
	jmp	LBB0_287
	.p2align	4, 0x90
LBB0_426:
	addl	$3, (%r14)
LBB0_287:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_288
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	addl	$-2, (%r14)
	jmp	LBB0_425
	.p2align	4, 0x90
LBB0_427:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	addl	$-4, (%r14)
LBB0_425:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_427
	jmp	LBB0_426
	.p2align	4, 0x90
LBB0_288:
	addl	$13, (%r14)
	jmp	LBB0_289
	.p2align	4, 0x90
LBB0_428:
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$5, (%r14)
LBB0_289:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_428
	.p2align	4, 0x90
LBB0_290:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_290
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$6, (%r14)
	jmp	LBB0_292
	.p2align	4, 0x90
LBB0_433:
	addl	$8, (%r14)
LBB0_292:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_293
	addl	$5, (%r14)
	jmp	LBB0_430
	.p2align	4, 0x90
LBB0_1389:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$4, (%r14)
LBB0_430:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1389
	addl	$-4, (%r14)
	jmp	LBB0_432
	.p2align	4, 0x90
LBB0_434:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_432:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_434
	jmp	LBB0_433
	.p2align	4, 0x90
LBB0_293:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_293
	addl	$9, (%r14)
	jmp	LBB0_295
	.p2align	4, 0x90
LBB0_437:
	addl	$7, (%r14)
LBB0_295:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_296
	addl	$2, (%r14)
	jmp	LBB0_436
	.p2align	4, 0x90
LBB0_438:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$9, (%r14)
LBB0_436:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_438
	jmp	LBB0_437
	.p2align	4, 0x90
LBB0_296:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_296
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	addb	$15, (%rbx,%rax)
	jmp	LBB0_298
	.p2align	4, 0x90
LBB0_443:
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_298:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_440
	jmp	LBB0_299
	.p2align	4, 0x90
LBB0_439:
	addl	$9, (%r14)
LBB0_440:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_439
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	.p2align	4, 0x90
LBB0_442:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_442
	jmp	LBB0_443
	.p2align	4, 0x90
LBB0_299:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_300
	.p2align	4, 0x90
LBB0_444:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_300:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_444
	.p2align	4, 0x90
LBB0_301:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_301
	addl	$9, (%r14)
	jmp	LBB0_303
	.p2align	4, 0x90
LBB0_454:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_303:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_304
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_446
	.p2align	4, 0x90
LBB0_1390:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_446:
	addl	$5, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1390
	addl	$-5, (%r14)
	jmp	LBB0_448
	.p2align	4, 0x90
LBB0_455:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-6, (%r14)
	jmp	LBB0_456
	.p2align	4, 0x90
LBB0_464:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$9, (%r14)
LBB0_456:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_457
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_461
	.p2align	4, 0x90
LBB0_1391:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_461:
	addl	$2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1391
	addl	$-2, (%r14)
	jmp	LBB0_463
	.p2align	4, 0x90
LBB0_465:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
LBB0_463:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_465
	jmp	LBB0_464
	.p2align	4, 0x90
LBB0_457:
	addl	$-8, (%r14)
	jmp	LBB0_458
	.p2align	4, 0x90
LBB0_459:
	addl	$-9, (%r14)
LBB0_458:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_459
LBB0_448:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_455
	.p2align	4, 0x90
LBB0_449:
	addl	$9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_449
	addl	$-9, (%r14)
	jmp	LBB0_451
	.p2align	4, 0x90
LBB0_468:
	addl	$-10, (%r14)
LBB0_451:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_452
	incl	(%r14)
	jmp	LBB0_467
	.p2align	4, 0x90
LBB0_469:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_467:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_469
	jmp	LBB0_468
	.p2align	4, 0x90
LBB0_452:
	incl	(%r14)
	jmp	LBB0_453
	.p2align	4, 0x90
LBB0_470:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_453:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_470
	jmp	LBB0_454
	.p2align	4, 0x90
LBB0_474:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_304:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_305
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_472
	.p2align	4, 0x90
LBB0_475:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_476
	.p2align	4, 0x90
LBB0_1392:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$7, (%r14)
LBB0_476:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1392
	jmp	LBB0_477
	.p2align	4, 0x90
LBB0_478:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_477:
	decl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_478
LBB0_472:
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_475
	jmp	LBB0_473
	.p2align	4, 0x90
LBB0_479:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_473:
	addl	$-2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_479
	jmp	LBB0_474
	.p2align	4, 0x90
LBB0_305:
	addl	$9, (%r14)
	jmp	LBB0_306
	.p2align	4, 0x90
LBB0_484:
	addl	$8, (%r14)
LBB0_306:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_307
	addl	$6, (%r14)
	jmp	LBB0_481
	.p2align	4, 0x90
LBB0_1393:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$5, (%r14)
LBB0_481:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1393
	addl	$-5, (%r14)
	jmp	LBB0_483
	.p2align	4, 0x90
LBB0_485:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_483:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_485
	jmp	LBB0_484
	.p2align	4, 0x90
LBB0_307:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_307
	addl	$9, (%r14)
	jmp	LBB0_309
	.p2align	4, 0x90
LBB0_486:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_309:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_486
	.p2align	4, 0x90
LBB0_310:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_310
	addl	$9, (%r14)
	jmp	LBB0_312
	.p2align	4, 0x90
LBB0_496:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_312:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_313
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_488
	.p2align	4, 0x90
LBB0_1394:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_488:
	addl	$5, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1394
	addl	$-5, (%r14)
	jmp	LBB0_490
	.p2align	4, 0x90
LBB0_497:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-6, (%r14)
	jmp	LBB0_498
	.p2align	4, 0x90
LBB0_506:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$9, (%r14)
LBB0_498:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_499
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_503
	.p2align	4, 0x90
LBB0_1395:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_503:
	addl	$2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1395
	addl	$-2, (%r14)
	jmp	LBB0_505
	.p2align	4, 0x90
LBB0_507:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
LBB0_505:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_507
	jmp	LBB0_506
	.p2align	4, 0x90
LBB0_499:
	addl	$-8, (%r14)
	jmp	LBB0_500
	.p2align	4, 0x90
LBB0_501:
	addl	$-9, (%r14)
LBB0_500:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_501
LBB0_490:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_497
	.p2align	4, 0x90
LBB0_491:
	addl	$9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_491
	addl	$-9, (%r14)
	jmp	LBB0_493
	.p2align	4, 0x90
LBB0_510:
	addl	$-10, (%r14)
LBB0_493:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_494
	incl	(%r14)
	jmp	LBB0_509
	.p2align	4, 0x90
LBB0_511:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_509:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_511
	jmp	LBB0_510
	.p2align	4, 0x90
LBB0_494:
	incl	(%r14)
	jmp	LBB0_495
	.p2align	4, 0x90
LBB0_512:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_495:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_512
	jmp	LBB0_496
	.p2align	4, 0x90
LBB0_516:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_313:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_314
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_514
	.p2align	4, 0x90
LBB0_517:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_518
	.p2align	4, 0x90
LBB0_1396:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$6, (%r14)
LBB0_518:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1396
	jmp	LBB0_519
	.p2align	4, 0x90
LBB0_520:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_519:
	decl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_520
LBB0_514:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_517
	jmp	LBB0_515
	.p2align	4, 0x90
LBB0_521:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_515:
	addl	$-3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_521
	jmp	LBB0_516
	.p2align	4, 0x90
LBB0_314:
	addl	$9, (%r14)
	jmp	LBB0_315
	.p2align	4, 0x90
LBB0_524:
	addl	$5, (%r14)
LBB0_315:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_316
	addl	$4, (%r14)
	jmp	LBB0_523
	.p2align	4, 0x90
LBB0_525:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-36, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$36, (%r14)
LBB0_523:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_525
	jmp	LBB0_524
	.p2align	4, 0x90
LBB0_316:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_316
	addl	$9, (%r14)
	jmp	LBB0_318
	.p2align	4, 0x90
LBB0_528:
	addl	$6, (%r14)
LBB0_318:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_319
	addl	$3, (%r14)
	jmp	LBB0_527
	.p2align	4, 0x90
LBB0_529:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-36, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$36, (%r14)
LBB0_527:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_529
	jmp	LBB0_528
	.p2align	4, 0x90
LBB0_319:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_319
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	addb	$15, (%rbx,%rax)
	jmp	LBB0_321
	.p2align	4, 0x90
LBB0_534:
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_321:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_531
	jmp	LBB0_322
	.p2align	4, 0x90
LBB0_530:
	addl	$9, (%r14)
LBB0_531:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_530
	movl	(%r14), %eax
	addl	$-9, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	.p2align	4, 0x90
LBB0_533:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_533
	jmp	LBB0_534
	.p2align	4, 0x90
LBB0_322:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_323
	.p2align	4, 0x90
LBB0_539:
	addl	$8, (%r14)
LBB0_323:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_324
	addl	$8, (%r14)
	jmp	LBB0_536
	.p2align	4, 0x90
LBB0_1397:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$7, (%r14)
LBB0_536:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1397
	addl	$-7, (%r14)
	jmp	LBB0_538
	.p2align	4, 0x90
LBB0_540:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_538:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_540
	jmp	LBB0_539
	.p2align	4, 0x90
LBB0_324:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_324
	addl	$9, (%r14)
	jmp	LBB0_326
	.p2align	4, 0x90
LBB0_541:
	movl	(%r14), %eax
	addl	$6, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$3, (%r14)
LBB0_326:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_541
	.p2align	4, 0x90
LBB0_327:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_327
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_329
	.p2align	4, 0x90
LBB0_542:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$5, (%r14)
LBB0_329:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_542
	jmp	LBB0_330
	.p2align	4, 0x90
LBB0_546:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_330:
	incl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_331
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	addl	$-6, (%r14)
	jmp	LBB0_544
	.p2align	4, 0x90
LBB0_1398:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	addb	$2, (%rbx,%rax)
	addl	$-4, (%r14)
LBB0_544:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1398
	jmp	LBB0_545
	.p2align	4, 0x90
LBB0_547:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_545:
	addl	$5, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_547
	jmp	LBB0_546
	.p2align	4, 0x90
LBB0_548:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_331:
	decl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_548
	jmp	LBB0_332
	.p2align	4, 0x90
LBB0_549:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_332:
	addl	$-5, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_549
	movl	(%r14), %eax
	addl	$6, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	jmp	LBB0_334
	.p2align	4, 0x90
LBB0_550:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_334:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_550
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
	.p2align	4, 0x90
LBB0_336:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_337
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_552
	.p2align	4, 0x90
LBB0_574:
	addl	$8, (%r14)
LBB0_552:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_565
	jmp	LBB0_553
	.p2align	4, 0x90
LBB0_564:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_565:
	addl	$2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_564
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
	.p2align	4, 0x90
LBB0_567:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_568
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_576
	.p2align	4, 0x90
LBB0_1399:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$3, (%r14)
LBB0_576:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1399
	addl	$-3, (%r14)
	jmp	LBB0_578
	.p2align	4, 0x90
LBB0_583:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_578:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_567
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-12, (%r14)
	jmp	LBB0_580
	.p2align	4, 0x90
LBB0_1400:
	addl	$-9, (%r14)
LBB0_580:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1400
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$6, (%r14)
	jmp	LBB0_582
	.p2align	4, 0x90
LBB0_584:
	addl	$9, (%r14)
LBB0_582:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_584
	jmp	LBB0_583
	.p2align	4, 0x90
LBB0_568:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_569
	.p2align	4, 0x90
LBB0_585:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_569:
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_585
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
	.p2align	4, 0x90
LBB0_571:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_572
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_587
	.p2align	4, 0x90
LBB0_1401:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$2, (%r14)
LBB0_587:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1401
	addl	$-2, (%r14)
	jmp	LBB0_589
	.p2align	4, 0x90
LBB0_594:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_589:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_571
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-11, (%r14)
	jmp	LBB0_591
	.p2align	4, 0x90
LBB0_1402:
	addl	$-9, (%r14)
LBB0_591:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1402
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_593
	.p2align	4, 0x90
LBB0_595:
	addl	$9, (%r14)
LBB0_593:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_595
	jmp	LBB0_594
	.p2align	4, 0x90
LBB0_572:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_573
	.p2align	4, 0x90
LBB0_598:
	addl	$-8, (%r14)
LBB0_573:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_574
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_597
	.p2align	4, 0x90
LBB0_599:
	addl	$9, (%r14)
LBB0_597:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_599
	jmp	LBB0_598
	.p2align	4, 0x90
LBB0_553:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_553
	jmp	LBB0_554
	.p2align	4, 0x90
LBB0_600:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_554:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_600
	jmp	LBB0_555
	.p2align	4, 0x90
LBB0_605:
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
LBB0_555:
	addl	$-4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_556
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_602
	.p2align	4, 0x90
LBB0_609:
	addl	$8, (%r14)
LBB0_602:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_603
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	jmp	LBB0_607
	.p2align	4, 0x90
LBB0_1403:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_607:
	addl	$2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1403
	jmp	LBB0_608
	.p2align	4, 0x90
LBB0_610:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_608:
	addl	$-2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_610
	jmp	LBB0_609
	.p2align	4, 0x90
LBB0_603:
	movl	(%r14), %eax
	addl	$-8, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_604
	.p2align	4, 0x90
LBB0_617:
	addl	$-12, (%r14)
LBB0_604:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_605
	incl	(%r14)
	jmp	LBB0_612
	.p2align	4, 0x90
LBB0_622:
	addl	$-2, (%r14)
LBB0_612:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_613
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
	jmp	LBB0_619
	.p2align	4, 0x90
LBB0_625:
	decl	(%r14)
LBB0_619:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_620
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-14, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
	jmp	LBB0_624
	.p2align	4, 0x90
LBB0_626:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
LBB0_624:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_626
	jmp	LBB0_625
	.p2align	4, 0x90
LBB0_620:
	incl	(%r14)
	jmp	LBB0_621
	.p2align	4, 0x90
LBB0_627:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-14, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
LBB0_621:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_627
	jmp	LBB0_622
	.p2align	4, 0x90
LBB0_613:
	incl	(%r14)
	jmp	LBB0_614
	.p2align	4, 0x90
LBB0_630:
	decl	(%r14)
LBB0_614:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_615
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
	jmp	LBB0_629
	.p2align	4, 0x90
LBB0_631:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-14, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
LBB0_629:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_631
	jmp	LBB0_630
	.p2align	4, 0x90
LBB0_615:
	incl	(%r14)
	jmp	LBB0_616
	.p2align	4, 0x90
LBB0_632:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
LBB0_616:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_632
	jmp	LBB0_617
	.p2align	4, 0x90
LBB0_633:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_556:
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_633
	addl	$-3, (%r14)
	jmp	LBB0_558
	.p2align	4, 0x90
LBB0_563:
	movl	(%r14), %eax
	addl	$6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-6, (%r14)
LBB0_558:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_336
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$6, (%r14)
	jmp	LBB0_560
	.p2align	4, 0x90
LBB0_637:
	addl	$8, (%r14)
LBB0_560:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_561
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	jmp	LBB0_635
	.p2align	4, 0x90
LBB0_1404:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_635:
	incl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1404
	jmp	LBB0_636
	.p2align	4, 0x90
LBB0_638:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_636:
	decl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_638
	jmp	LBB0_637
	.p2align	4, 0x90
LBB0_561:
	movl	(%r14), %eax
	addl	$-8, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_562
	.p2align	4, 0x90
LBB0_645:
	addl	$-11, (%r14)
LBB0_562:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_563
	incl	(%r14)
	jmp	LBB0_640
	.p2align	4, 0x90
LBB0_650:
	decl	(%r14)
LBB0_640:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_641
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
	jmp	LBB0_647
	.p2align	4, 0x90
LBB0_653:
	incl	(%r14)
LBB0_647:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_648
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-14, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$10, (%r14)
	jmp	LBB0_652
	.p2align	4, 0x90
LBB0_654:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
LBB0_652:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_654
	jmp	LBB0_653
	.p2align	4, 0x90
LBB0_648:
	decl	(%r14)
	jmp	LBB0_649
	.p2align	4, 0x90
LBB0_655:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-14, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$10, (%r14)
LBB0_649:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_655
	jmp	LBB0_650
	.p2align	4, 0x90
LBB0_641:
	addl	$2, (%r14)
	jmp	LBB0_642
	.p2align	4, 0x90
LBB0_658:
	incl	(%r14)
LBB0_642:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_643
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
	jmp	LBB0_657
	.p2align	4, 0x90
LBB0_659:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-14, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$10, (%r14)
LBB0_657:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_659
	jmp	LBB0_658
	.p2align	4, 0x90
LBB0_643:
	decl	(%r14)
	jmp	LBB0_644
	.p2align	4, 0x90
LBB0_660:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
LBB0_644:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_660
	jmp	LBB0_645
	.p2align	4, 0x90
LBB0_661:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_337:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_661
	addl	$-4, (%r14)
	.p2align	4, 0x90
LBB0_339:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_340
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_663
	.p2align	4, 0x90
LBB0_1405:
	addl	$9, (%r14)
LBB0_663:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1405
	addl	$-9, (%r14)
	jmp	LBB0_665
	.p2align	4, 0x90
LBB0_672:
	addl	$-12, (%r14)
LBB0_665:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_339
	incl	(%r14)
	jmp	LBB0_667
	.p2align	4, 0x90
LBB0_677:
	addl	$-2, (%r14)
LBB0_667:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_668
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
	jmp	LBB0_674
	.p2align	4, 0x90
LBB0_680:
	decl	(%r14)
LBB0_674:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_675
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-14, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
	jmp	LBB0_679
	.p2align	4, 0x90
LBB0_681:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
LBB0_679:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_681
	jmp	LBB0_680
	.p2align	4, 0x90
LBB0_675:
	incl	(%r14)
	jmp	LBB0_676
	.p2align	4, 0x90
LBB0_682:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-14, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
LBB0_676:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_682
	jmp	LBB0_677
	.p2align	4, 0x90
LBB0_668:
	incl	(%r14)
	jmp	LBB0_669
	.p2align	4, 0x90
LBB0_685:
	decl	(%r14)
LBB0_669:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_670
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
	jmp	LBB0_684
	.p2align	4, 0x90
LBB0_686:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-14, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
LBB0_684:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_686
	jmp	LBB0_685
	.p2align	4, 0x90
LBB0_670:
	incl	(%r14)
	jmp	LBB0_671
	.p2align	4, 0x90
LBB0_687:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
LBB0_671:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_687
	jmp	LBB0_672
	.p2align	4, 0x90
LBB0_340:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_341
	.p2align	4, 0x90
LBB0_688:
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$6, (%r14)
LBB0_341:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_688
	.p2align	4, 0x90
LBB0_342:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_342
	addl	$9, (%r14)
	jmp	LBB0_344
	.p2align	4, 0x90
LBB0_693:
	addl	$8, (%r14)
LBB0_344:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_345
	addl	$5, (%r14)
	jmp	LBB0_690
	.p2align	4, 0x90
LBB0_1406:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$4, (%r14)
LBB0_690:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1406
	addl	$-4, (%r14)
	jmp	LBB0_692
	.p2align	4, 0x90
LBB0_694:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_692:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_694
	jmp	LBB0_693
	.p2align	4, 0x90
LBB0_345:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_345
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	addb	$15, (%rbx,%rax)
	jmp	LBB0_347
	.p2align	4, 0x90
LBB0_699:
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_347:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_696
	jmp	LBB0_348
	.p2align	4, 0x90
LBB0_695:
	addl	$9, (%r14)
LBB0_696:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_695
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	.p2align	4, 0x90
LBB0_698:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_698
	jmp	LBB0_699
	.p2align	4, 0x90
LBB0_348:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_349
	.p2align	4, 0x90
LBB0_700:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_349:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_700
	.p2align	4, 0x90
LBB0_350:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_350
	addl	$9, (%r14)
	jmp	LBB0_352
	.p2align	4, 0x90
LBB0_710:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_352:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_353
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_702
	.p2align	4, 0x90
LBB0_1407:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_702:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1407
	addl	$-4, (%r14)
	jmp	LBB0_704
	.p2align	4, 0x90
LBB0_711:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-5, (%r14)
	jmp	LBB0_712
	.p2align	4, 0x90
LBB0_720:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$9, (%r14)
LBB0_712:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_713
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_717
	.p2align	4, 0x90
LBB0_1408:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_717:
	addl	$2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1408
	addl	$-2, (%r14)
	jmp	LBB0_719
	.p2align	4, 0x90
LBB0_721:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
LBB0_719:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_721
	jmp	LBB0_720
	.p2align	4, 0x90
LBB0_713:
	addl	$-8, (%r14)
	jmp	LBB0_714
	.p2align	4, 0x90
LBB0_715:
	addl	$-9, (%r14)
LBB0_714:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_715
LBB0_704:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_711
	.p2align	4, 0x90
LBB0_705:
	addl	$9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_705
	addl	$-9, (%r14)
	jmp	LBB0_707
	.p2align	4, 0x90
LBB0_724:
	addl	$-10, (%r14)
LBB0_707:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_708
	incl	(%r14)
	jmp	LBB0_723
	.p2align	4, 0x90
LBB0_725:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_723:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_725
	jmp	LBB0_724
	.p2align	4, 0x90
LBB0_708:
	incl	(%r14)
	jmp	LBB0_709
	.p2align	4, 0x90
LBB0_726:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_709:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_726
	jmp	LBB0_710
	.p2align	4, 0x90
LBB0_730:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_353:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_354
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_728
	.p2align	4, 0x90
LBB0_731:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_732
	.p2align	4, 0x90
LBB0_1409:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$7, (%r14)
LBB0_732:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1409
	jmp	LBB0_733
	.p2align	4, 0x90
LBB0_734:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_733:
	decl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_734
LBB0_728:
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_731
	jmp	LBB0_729
	.p2align	4, 0x90
LBB0_735:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_729:
	addl	$-2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_735
	jmp	LBB0_730
	.p2align	4, 0x90
LBB0_354:
	addl	$9, (%r14)
	jmp	LBB0_355
	.p2align	4, 0x90
LBB0_738:
	addl	$6, (%r14)
LBB0_355:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_356
	addl	$3, (%r14)
	jmp	LBB0_737
	.p2align	4, 0x90
LBB0_739:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-36, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$36, (%r14)
LBB0_737:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_739
	jmp	LBB0_738
	.p2align	4, 0x90
LBB0_356:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_356
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	addb	$15, (%rbx,%rax)
	jmp	LBB0_358
	.p2align	4, 0x90
LBB0_744:
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_358:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_741
	jmp	LBB0_359
	.p2align	4, 0x90
LBB0_740:
	addl	$9, (%r14)
LBB0_741:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_740
	movl	(%r14), %eax
	addl	$-9, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	.p2align	4, 0x90
LBB0_743:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_743
	jmp	LBB0_744
	.p2align	4, 0x90
LBB0_359:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_360
	.p2align	4, 0x90
LBB0_755:
	addl	$8, (%r14)
LBB0_360:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_746
	jmp	LBB0_361
	.p2align	4, 0x90
LBB0_745:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_746:
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_745
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
	.p2align	4, 0x90
LBB0_748:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_749
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_757
	.p2align	4, 0x90
LBB0_1410:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$4, (%r14)
LBB0_757:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1410
	addl	$-4, (%r14)
	jmp	LBB0_759
	.p2align	4, 0x90
LBB0_764:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_759:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_748
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-13, (%r14)
	jmp	LBB0_761
	.p2align	4, 0x90
LBB0_1411:
	addl	$-9, (%r14)
LBB0_761:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1411
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_763
	.p2align	4, 0x90
LBB0_765:
	addl	$9, (%r14)
LBB0_763:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_765
	jmp	LBB0_764
	.p2align	4, 0x90
LBB0_749:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_750
	.p2align	4, 0x90
LBB0_766:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_750:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_766
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
	.p2align	4, 0x90
LBB0_752:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_753
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_768
	.p2align	4, 0x90
LBB0_1412:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$3, (%r14)
LBB0_768:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1412
	addl	$-3, (%r14)
	jmp	LBB0_770
	.p2align	4, 0x90
LBB0_775:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_770:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_752
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-12, (%r14)
	jmp	LBB0_772
	.p2align	4, 0x90
LBB0_1413:
	addl	$-9, (%r14)
LBB0_772:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1413
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$6, (%r14)
	jmp	LBB0_774
	.p2align	4, 0x90
LBB0_776:
	addl	$9, (%r14)
LBB0_774:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_776
	jmp	LBB0_775
	.p2align	4, 0x90
LBB0_753:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_754
	.p2align	4, 0x90
LBB0_779:
	addl	$-8, (%r14)
LBB0_754:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_755
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_778
	.p2align	4, 0x90
LBB0_780:
	addl	$9, (%r14)
LBB0_778:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_780
	jmp	LBB0_779
	.p2align	4, 0x90
LBB0_361:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_361
	jmp	LBB0_362
	.p2align	4, 0x90
LBB0_781:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_362:
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_781
	addl	$-3, (%r14)
	.p2align	4, 0x90
LBB0_364:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_365
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$6, (%r14)
	jmp	LBB0_783
	.p2align	4, 0x90
LBB0_796:
	addl	$8, (%r14)
LBB0_783:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_784
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	jmp	LBB0_794
	.p2align	4, 0x90
LBB0_1414:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_794:
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1414
	jmp	LBB0_795
	.p2align	4, 0x90
LBB0_797:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_795:
	addl	$-3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_797
	jmp	LBB0_796
	.p2align	4, 0x90
LBB0_784:
	movl	(%r14), %eax
	addl	$-8, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_785
	.p2align	4, 0x90
LBB0_792:
	addl	$-13, (%r14)
LBB0_785:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_364
	incl	(%r14)
	jmp	LBB0_787
	.p2align	4, 0x90
LBB0_802:
	addl	$-3, (%r14)
LBB0_787:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_788
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_799
	.p2align	4, 0x90
LBB0_805:
	decl	(%r14)
LBB0_799:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_800
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-10, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$12, (%r14)
	jmp	LBB0_804
	.p2align	4, 0x90
LBB0_806:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$2, (%r14)
LBB0_804:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_806
	jmp	LBB0_805
	.p2align	4, 0x90
LBB0_800:
	incl	(%r14)
	jmp	LBB0_801
	.p2align	4, 0x90
LBB0_807:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-10, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$12, (%r14)
LBB0_801:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_807
	jmp	LBB0_802
	.p2align	4, 0x90
LBB0_788:
	addl	$2, (%r14)
	jmp	LBB0_789
	.p2align	4, 0x90
LBB0_810:
	decl	(%r14)
LBB0_789:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_790
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$2, (%r14)
	jmp	LBB0_809
	.p2align	4, 0x90
LBB0_811:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-10, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$12, (%r14)
LBB0_809:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_811
	jmp	LBB0_810
	.p2align	4, 0x90
LBB0_790:
	incl	(%r14)
	jmp	LBB0_791
	.p2align	4, 0x90
LBB0_812:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$2, (%r14)
LBB0_791:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_812
	jmp	LBB0_792
	.p2align	4, 0x90
LBB0_813:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_365:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_813
	addl	$-4, (%r14)
	jmp	LBB0_367
	.p2align	4, 0x90
LBB0_818:
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-5, (%r14)
LBB0_367:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_368
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_815
	.p2align	4, 0x90
LBB0_822:
	addl	$8, (%r14)
LBB0_815:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_816
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	jmp	LBB0_820
	.p2align	4, 0x90
LBB0_1415:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_820:
	addl	$2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1415
	jmp	LBB0_821
	.p2align	4, 0x90
LBB0_823:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_821:
	addl	$-2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_823
	jmp	LBB0_822
	.p2align	4, 0x90
LBB0_816:
	movl	(%r14), %eax
	addl	$-8, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_817
	.p2align	4, 0x90
LBB0_830:
	addl	$-12, (%r14)
LBB0_817:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_818
	incl	(%r14)
	jmp	LBB0_825
	.p2align	4, 0x90
LBB0_835:
	addl	$-2, (%r14)
LBB0_825:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_826
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$2, (%r14)
	jmp	LBB0_832
	.p2align	4, 0x90
LBB0_838:
	incl	(%r14)
LBB0_832:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_833
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-10, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
	jmp	LBB0_837
	.p2align	4, 0x90
LBB0_839:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
LBB0_837:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_839
	jmp	LBB0_838
	.p2align	4, 0x90
LBB0_833:
	decl	(%r14)
	jmp	LBB0_834
	.p2align	4, 0x90
LBB0_840:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-10, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
LBB0_834:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_840
	jmp	LBB0_835
	.p2align	4, 0x90
LBB0_826:
	addl	$3, (%r14)
	jmp	LBB0_827
	.p2align	4, 0x90
LBB0_843:
	incl	(%r14)
LBB0_827:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_828
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_842
	.p2align	4, 0x90
LBB0_844:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-10, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
LBB0_842:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_844
	jmp	LBB0_843
	.p2align	4, 0x90
LBB0_828:
	decl	(%r14)
	jmp	LBB0_829
	.p2align	4, 0x90
LBB0_845:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
LBB0_829:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_845
	jmp	LBB0_830
	.p2align	4, 0x90
LBB0_368:
	addl	$9, (%r14)
	jmp	LBB0_369
	.p2align	4, 0x90
LBB0_846:
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$4, (%r14)
LBB0_369:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_846
	.p2align	4, 0x90
LBB0_370:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_370
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_372
	.p2align	4, 0x90
LBB0_851:
	addl	$8, (%r14)
LBB0_372:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_373
	addl	$7, (%r14)
	jmp	LBB0_848
	.p2align	4, 0x90
LBB0_1416:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$6, (%r14)
LBB0_848:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1416
	addl	$-6, (%r14)
	jmp	LBB0_850
	.p2align	4, 0x90
LBB0_852:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
LBB0_850:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_852
	jmp	LBB0_851
	.p2align	4, 0x90
LBB0_373:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_373
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_375
	.p2align	4, 0x90
LBB0_853:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$5, (%r14)
LBB0_375:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_853
	jmp	LBB0_376
	.p2align	4, 0x90
LBB0_857:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_376:
	addl	$2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_377
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	addl	$-7, (%r14)
	jmp	LBB0_855
	.p2align	4, 0x90
LBB0_1417:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	addb	$2, (%rbx,%rax)
	addl	$-4, (%r14)
LBB0_855:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1417
	jmp	LBB0_856
	.p2align	4, 0x90
LBB0_858:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_856:
	addl	$5, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_858
	jmp	LBB0_857
	.p2align	4, 0x90
LBB0_859:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_377:
	addl	$-2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_859
	jmp	LBB0_378
	.p2align	4, 0x90
LBB0_860:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_378:
	addl	$-5, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_860
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_380
	.p2align	4, 0x90
LBB0_861:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_380:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_861
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_382
	.p2align	4, 0x90
LBB0_871:
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
LBB0_382:
	addl	$-4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_383
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_863
	.p2align	4, 0x90
LBB0_882:
	addl	$8, (%r14)
LBB0_863:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_873
	jmp	LBB0_864
	.p2align	4, 0x90
LBB0_872:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_873:
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_872
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
	.p2align	4, 0x90
LBB0_875:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_876
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_884
	.p2align	4, 0x90
LBB0_1418:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$2, (%r14)
LBB0_884:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1418
	addl	$-2, (%r14)
	jmp	LBB0_886
	.p2align	4, 0x90
LBB0_891:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_886:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_875
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-11, (%r14)
	jmp	LBB0_888
	.p2align	4, 0x90
LBB0_1419:
	addl	$-9, (%r14)
LBB0_888:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1419
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_890
	.p2align	4, 0x90
LBB0_892:
	addl	$9, (%r14)
LBB0_890:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_892
	jmp	LBB0_891
	.p2align	4, 0x90
LBB0_876:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_877
	.p2align	4, 0x90
LBB0_893:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_877:
	addl	$2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_893
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
	.p2align	4, 0x90
LBB0_879:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_880
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_895
	.p2align	4, 0x90
LBB0_1420:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$3, (%r14)
LBB0_895:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1420
	addl	$-3, (%r14)
	jmp	LBB0_897
	.p2align	4, 0x90
LBB0_902:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_897:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_879
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-12, (%r14)
	jmp	LBB0_899
	.p2align	4, 0x90
LBB0_1421:
	addl	$-9, (%r14)
LBB0_899:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1421
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$6, (%r14)
	jmp	LBB0_901
	.p2align	4, 0x90
LBB0_903:
	addl	$9, (%r14)
LBB0_901:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_903
	jmp	LBB0_902
	.p2align	4, 0x90
LBB0_880:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_881
	.p2align	4, 0x90
LBB0_906:
	addl	$-8, (%r14)
LBB0_881:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_882
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_905
	.p2align	4, 0x90
LBB0_907:
	addl	$9, (%r14)
LBB0_905:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_907
	jmp	LBB0_906
	.p2align	4, 0x90
LBB0_864:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_864
	jmp	LBB0_865
	.p2align	4, 0x90
LBB0_908:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_865:
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_908
	addl	$-3, (%r14)
	jmp	LBB0_867
	.p2align	4, 0x90
LBB0_909:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$6, (%r14)
	jmp	LBB0_910
	.p2align	4, 0x90
LBB0_921:
	addl	$8, (%r14)
LBB0_910:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_911
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	jmp	LBB0_919
	.p2align	4, 0x90
LBB0_1422:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_919:
	incl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1422
	jmp	LBB0_920
	.p2align	4, 0x90
LBB0_922:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_920:
	decl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_922
	jmp	LBB0_921
	.p2align	4, 0x90
LBB0_911:
	movl	(%r14), %eax
	addl	$-8, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_912
	.p2align	4, 0x90
LBB0_929:
	addl	$-11, (%r14)
LBB0_912:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_913
	incl	(%r14)
	jmp	LBB0_924
	.p2align	4, 0x90
LBB0_934:
	decl	(%r14)
LBB0_924:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_925
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
	jmp	LBB0_931
	.p2align	4, 0x90
LBB0_937:
	incl	(%r14)
LBB0_931:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_932
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-13, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$10, (%r14)
	jmp	LBB0_936
	.p2align	4, 0x90
LBB0_938:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
LBB0_936:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_938
	jmp	LBB0_937
	.p2align	4, 0x90
LBB0_932:
	decl	(%r14)
	jmp	LBB0_933
	.p2align	4, 0x90
LBB0_939:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-13, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$10, (%r14)
LBB0_933:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_939
	jmp	LBB0_934
	.p2align	4, 0x90
LBB0_925:
	addl	$2, (%r14)
	jmp	LBB0_926
	.p2align	4, 0x90
LBB0_942:
	incl	(%r14)
LBB0_926:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_927
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
	jmp	LBB0_941
	.p2align	4, 0x90
LBB0_943:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-13, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$10, (%r14)
LBB0_941:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_943
	jmp	LBB0_942
	.p2align	4, 0x90
LBB0_927:
	decl	(%r14)
	jmp	LBB0_928
	.p2align	4, 0x90
LBB0_944:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
LBB0_928:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_944
	jmp	LBB0_929
	.p2align	4, 0x90
LBB0_913:
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$2, (%r14)
	jmp	LBB0_914
	.p2align	4, 0x90
LBB0_945:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$7, (%r14)
LBB0_914:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_945
	addl	$-7, (%r14)
	jmp	LBB0_916
	.p2align	4, 0x90
LBB0_917:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-5, (%r14)
LBB0_916:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_917
LBB0_867:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_909
	jmp	LBB0_868
	.p2align	4, 0x90
LBB0_946:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_868:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_946
	addl	$-4, (%r14)
	.p2align	4, 0x90
LBB0_870:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_871
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_948
	.p2align	4, 0x90
LBB0_961:
	addl	$8, (%r14)
LBB0_948:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_949
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	jmp	LBB0_959
	.p2align	4, 0x90
LBB0_1423:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_959:
	addl	$2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1423
	jmp	LBB0_960
	.p2align	4, 0x90
LBB0_962:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_960:
	addl	$-2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_962
	jmp	LBB0_961
	.p2align	4, 0x90
LBB0_949:
	movl	(%r14), %eax
	addl	$-8, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_950
	.p2align	4, 0x90
LBB0_957:
	addl	$-12, (%r14)
LBB0_950:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_870
	incl	(%r14)
	jmp	LBB0_952
	.p2align	4, 0x90
LBB0_967:
	addl	$-2, (%r14)
LBB0_952:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_953
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
	jmp	LBB0_964
	.p2align	4, 0x90
LBB0_970:
	decl	(%r14)
LBB0_964:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_965
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-13, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
	jmp	LBB0_969
	.p2align	4, 0x90
LBB0_971:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
LBB0_969:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_971
	jmp	LBB0_970
	.p2align	4, 0x90
LBB0_965:
	incl	(%r14)
	jmp	LBB0_966
	.p2align	4, 0x90
LBB0_972:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-13, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
LBB0_966:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_972
	jmp	LBB0_967
	.p2align	4, 0x90
LBB0_953:
	incl	(%r14)
	jmp	LBB0_954
	.p2align	4, 0x90
LBB0_975:
	decl	(%r14)
LBB0_954:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_955
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
	jmp	LBB0_974
	.p2align	4, 0x90
LBB0_976:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-13, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
LBB0_974:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_976
	jmp	LBB0_975
	.p2align	4, 0x90
LBB0_955:
	incl	(%r14)
	jmp	LBB0_956
	.p2align	4, 0x90
LBB0_977:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
LBB0_956:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_977
	jmp	LBB0_957
	.p2align	4, 0x90
LBB0_978:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_383:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_978
	addl	$-4, (%r14)
	.p2align	4, 0x90
LBB0_385:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_386
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$2, (%r14)
	jmp	LBB0_980
	.p2align	4, 0x90
LBB0_1424:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$7, (%r14)
LBB0_980:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1424
	addl	$-7, (%r14)
	jmp	LBB0_982
	.p2align	4, 0x90
LBB0_1425:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-5, (%r14)
LBB0_982:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1425
	.p2align	4, 0x90
LBB0_983:
	addl	$9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_983
	addl	$-9, (%r14)
	jmp	LBB0_985
	.p2align	4, 0x90
LBB0_992:
	addl	$-12, (%r14)
LBB0_985:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_385
	incl	(%r14)
	jmp	LBB0_987
	.p2align	4, 0x90
LBB0_997:
	addl	$-2, (%r14)
LBB0_987:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_988
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
	jmp	LBB0_994
	.p2align	4, 0x90
LBB0_1000:
	decl	(%r14)
LBB0_994:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_995
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-13, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
	jmp	LBB0_999
	.p2align	4, 0x90
LBB0_1001:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
LBB0_999:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1001
	jmp	LBB0_1000
	.p2align	4, 0x90
LBB0_995:
	incl	(%r14)
	jmp	LBB0_996
	.p2align	4, 0x90
LBB0_1002:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-13, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
LBB0_996:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1002
	jmp	LBB0_997
	.p2align	4, 0x90
LBB0_988:
	incl	(%r14)
	jmp	LBB0_989
	.p2align	4, 0x90
LBB0_1005:
	decl	(%r14)
LBB0_989:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_990
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
	jmp	LBB0_1004
	.p2align	4, 0x90
LBB0_1006:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-13, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$11, (%r14)
LBB0_1004:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1006
	jmp	LBB0_1005
	.p2align	4, 0x90
LBB0_990:
	incl	(%r14)
	jmp	LBB0_991
	.p2align	4, 0x90
LBB0_1007:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
LBB0_991:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1007
	jmp	LBB0_992
	.p2align	4, 0x90
LBB0_386:
	addl	$9, (%r14)
	jmp	LBB0_387
	.p2align	4, 0x90
LBB0_1008:
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$6, (%r14)
LBB0_387:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1008
	.p2align	4, 0x90
LBB0_388:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_388
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_390
	.p2align	4, 0x90
LBB0_1013:
	addl	$8, (%r14)
LBB0_390:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_391
	addl	$5, (%r14)
	jmp	LBB0_1010
	.p2align	4, 0x90
LBB0_1426:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$4, (%r14)
LBB0_1010:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1426
	addl	$-4, (%r14)
	jmp	LBB0_1012
	.p2align	4, 0x90
LBB0_1014:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_1012:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1014
	jmp	LBB0_1013
	.p2align	4, 0x90
LBB0_391:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_391
	addl	$9, (%r14)
	jmp	LBB0_393
	.p2align	4, 0x90
LBB0_1019:
	addl	$8, (%r14)
LBB0_393:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_394
	addl	$6, (%r14)
	jmp	LBB0_1016
	.p2align	4, 0x90
LBB0_1427:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$5, (%r14)
LBB0_1016:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1427
	addl	$-5, (%r14)
	jmp	LBB0_1018
	.p2align	4, 0x90
LBB0_1020:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
LBB0_1018:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1020
	jmp	LBB0_1019
	.p2align	4, 0x90
LBB0_394:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_394
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	addb	$15, (%rbx,%rax)
	jmp	LBB0_396
	.p2align	4, 0x90
LBB0_1025:
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_396:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1022
	jmp	LBB0_397
	.p2align	4, 0x90
LBB0_1021:
	addl	$9, (%r14)
LBB0_1022:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1021
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	.p2align	4, 0x90
LBB0_1024:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1024
	jmp	LBB0_1025
	.p2align	4, 0x90
LBB0_397:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_398
	.p2align	4, 0x90
LBB0_1026:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_398:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1026
	.p2align	4, 0x90
LBB0_399:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_399
	addl	$9, (%r14)
	jmp	LBB0_401
	.p2align	4, 0x90
LBB0_1036:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_401:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_402
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_1028
	.p2align	4, 0x90
LBB0_1428:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1028:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1428
	addl	$-4, (%r14)
	jmp	LBB0_1030
	.p2align	4, 0x90
LBB0_1037:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-5, (%r14)
	jmp	LBB0_1038
	.p2align	4, 0x90
LBB0_1046:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$9, (%r14)
LBB0_1038:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1039
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_1043
	.p2align	4, 0x90
LBB0_1429:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1043:
	addl	$2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1429
	addl	$-2, (%r14)
	jmp	LBB0_1045
	.p2align	4, 0x90
LBB0_1047:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
LBB0_1045:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1047
	jmp	LBB0_1046
	.p2align	4, 0x90
LBB0_1039:
	addl	$-8, (%r14)
	jmp	LBB0_1040
	.p2align	4, 0x90
LBB0_1041:
	addl	$-9, (%r14)
LBB0_1040:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1041
LBB0_1030:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1037
	.p2align	4, 0x90
LBB0_1031:
	addl	$9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1031
	addl	$-9, (%r14)
	jmp	LBB0_1033
	.p2align	4, 0x90
LBB0_1050:
	addl	$-10, (%r14)
LBB0_1033:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1034
	incl	(%r14)
	jmp	LBB0_1049
	.p2align	4, 0x90
LBB0_1051:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_1049:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1051
	jmp	LBB0_1050
	.p2align	4, 0x90
LBB0_1034:
	incl	(%r14)
	jmp	LBB0_1035
	.p2align	4, 0x90
LBB0_1052:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_1035:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1052
	jmp	LBB0_1036
	.p2align	4, 0x90
LBB0_1056:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_402:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_403
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_1054
	.p2align	4, 0x90
LBB0_1057:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_1058
	.p2align	4, 0x90
LBB0_1430:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$6, (%r14)
LBB0_1058:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1430
	jmp	LBB0_1059
	.p2align	4, 0x90
LBB0_1060:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1059:
	decl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1060
LBB0_1054:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1057
	jmp	LBB0_1055
	.p2align	4, 0x90
LBB0_1061:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1055:
	addl	$-3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1061
	jmp	LBB0_1056
	.p2align	4, 0x90
LBB0_403:
	addl	$9, (%r14)
	jmp	LBB0_404
	.p2align	4, 0x90
LBB0_1062:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_404:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1062
	.p2align	4, 0x90
LBB0_405:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_405
	addl	$9, (%r14)
	jmp	LBB0_407
	.p2align	4, 0x90
LBB0_1072:
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_407:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_408
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_1064
	.p2align	4, 0x90
LBB0_1431:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1064:
	addl	$5, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1431
	addl	$-5, (%r14)
	jmp	LBB0_1066
	.p2align	4, 0x90
LBB0_1073:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-6, (%r14)
	jmp	LBB0_1074
	.p2align	4, 0x90
LBB0_1082:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$9, (%r14)
LBB0_1074:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1075
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_1079
	.p2align	4, 0x90
LBB0_1432:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1079:
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1432
	addl	$-3, (%r14)
	jmp	LBB0_1081
	.p2align	4, 0x90
LBB0_1083:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
LBB0_1081:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1083
	jmp	LBB0_1082
	.p2align	4, 0x90
LBB0_1075:
	addl	$-8, (%r14)
	jmp	LBB0_1076
	.p2align	4, 0x90
LBB0_1077:
	addl	$-9, (%r14)
LBB0_1076:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1077
LBB0_1066:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1073
	.p2align	4, 0x90
LBB0_1067:
	addl	$9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1067
	addl	$-9, (%r14)
	jmp	LBB0_1069
	.p2align	4, 0x90
LBB0_1086:
	addl	$-11, (%r14)
LBB0_1069:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1070
	addl	$2, (%r14)
	jmp	LBB0_1085
	.p2align	4, 0x90
LBB0_1087:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_1085:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1087
	jmp	LBB0_1086
	.p2align	4, 0x90
LBB0_1070:
	addl	$2, (%r14)
	jmp	LBB0_1071
	.p2align	4, 0x90
LBB0_1088:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_1071:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1088
	jmp	LBB0_1072
	.p2align	4, 0x90
LBB0_1092:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_408:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_409
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_1090
	.p2align	4, 0x90
LBB0_1093:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_1094
	.p2align	4, 0x90
LBB0_1433:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$6, (%r14)
LBB0_1094:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1433
	jmp	LBB0_1095
	.p2align	4, 0x90
LBB0_1096:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1095:
	decl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1096
LBB0_1090:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1093
	jmp	LBB0_1091
	.p2align	4, 0x90
LBB0_1097:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1091:
	addl	$-3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1097
	jmp	LBB0_1092
	.p2align	4, 0x90
LBB0_409:
	addl	$9, (%r14)
	jmp	LBB0_410
	.p2align	4, 0x90
LBB0_1100:
	addl	$5, (%r14)
LBB0_410:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_411
	addl	$4, (%r14)
	jmp	LBB0_1099
	.p2align	4, 0x90
LBB0_1101:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-36, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$36, (%r14)
LBB0_1099:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1101
	jmp	LBB0_1100
	.p2align	4, 0x90
LBB0_411:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_411
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	addb	$15, (%rbx,%rax)
	jmp	LBB0_413
	.p2align	4, 0x90
LBB0_1106:
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_413:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1103
	jmp	LBB0_414
	.p2align	4, 0x90
LBB0_1102:
	addl	$9, (%r14)
LBB0_1103:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1102
	movl	(%r14), %eax
	addl	$-9, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	.p2align	4, 0x90
LBB0_1105:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1105
	jmp	LBB0_1106
	.p2align	4, 0x90
LBB0_414:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$21, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
	jmp	LBB0_415
	.p2align	4, 0x90
LBB0_1107:
	addl	$-9, (%r14)
LBB0_415:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1107
	addl	$9, (%r14)
	jmp	LBB0_417
	.p2align	4, 0x90
LBB0_1118:
	addl	$8, (%r14)
LBB0_417:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1109
	jmp	LBB0_418
	.p2align	4, 0x90
LBB0_1108:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_1109:
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1108
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
	.p2align	4, 0x90
LBB0_1111:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1112
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_1120
	.p2align	4, 0x90
LBB0_1434:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$4, (%r14)
LBB0_1120:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1434
	addl	$-4, (%r14)
	jmp	LBB0_1122
	.p2align	4, 0x90
LBB0_1127:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_1122:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1111
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-13, (%r14)
	jmp	LBB0_1124
	.p2align	4, 0x90
LBB0_1435:
	addl	$-9, (%r14)
LBB0_1124:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1435
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_1126
	.p2align	4, 0x90
LBB0_1128:
	addl	$9, (%r14)
LBB0_1126:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1128
	jmp	LBB0_1127
	.p2align	4, 0x90
LBB0_1112:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_1113
	.p2align	4, 0x90
LBB0_1129:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_1113:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1129
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
	.p2align	4, 0x90
LBB0_1115:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1116
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_1131
	.p2align	4, 0x90
LBB0_1436:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$3, (%r14)
LBB0_1131:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1436
	addl	$-3, (%r14)
	jmp	LBB0_1133
	.p2align	4, 0x90
LBB0_1138:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_1133:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1115
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-12, (%r14)
	jmp	LBB0_1135
	.p2align	4, 0x90
LBB0_1437:
	addl	$-9, (%r14)
LBB0_1135:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1437
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$6, (%r14)
	jmp	LBB0_1137
	.p2align	4, 0x90
LBB0_1139:
	addl	$9, (%r14)
LBB0_1137:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1139
	jmp	LBB0_1138
	.p2align	4, 0x90
LBB0_1116:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_1117
	.p2align	4, 0x90
LBB0_1142:
	addl	$-8, (%r14)
LBB0_1117:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1118
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_1141
	.p2align	4, 0x90
LBB0_1143:
	addl	$9, (%r14)
LBB0_1141:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1143
	jmp	LBB0_1142
	.p2align	4, 0x90
LBB0_418:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_418
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	addl	$2, (%r14)
	jmp	LBB0_420
	.p2align	4, 0x90
LBB0_1144:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$4, (%r14)
LBB0_420:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1144
	addl	$-4, (%r14)
	jmp	LBB0_422
	.p2align	4, 0x90
LBB0_423:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$-2, (%r14)
LBB0_422:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_423
LBB0_102:
	addl	$2, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_284
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	jmp	LBB0_104
	.p2align	4, 0x90
LBB0_1145:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_104:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1145
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-4, (%r14)
	jmp	LBB0_106
	.p2align	4, 0x90
LBB0_1146:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	movzbl	(%rbx,%rax), %edi
	movl	$1, %esi
	callq	*%r15
	addl	$2, (%r14)
LBB0_106:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1146
	addl	$4, (%r14)
	jmp	LBB0_108
	.p2align	4, 0x90
LBB0_1147:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	movzbl	(%rbx,%rax), %edi
	movl	$1, %esi
	callq	*%r15
	addl	$7, (%r14)
LBB0_108:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1147
	movl	(%r14), %eax
	addl	$-3, %eax
	jmp	LBB0_110
	.p2align	4, 0x90
LBB0_1148:
	movl	(%r14), %eax
	incl	%eax
LBB0_110:
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1148
	.p2align	4, 0x90
LBB0_111:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_111
	addl	$9, (%r14)
	jmp	LBB0_113
	.p2align	4, 0x90
LBB0_1149:
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$4, (%r14)
LBB0_113:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1149
	.p2align	4, 0x90
LBB0_114:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_114
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	addb	$11, (%rbx,%rax)
	jmp	LBB0_116
	.p2align	4, 0x90
LBB0_1152:
	addl	$9, (%r14)
LBB0_116:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_117
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_1151
	.p2align	4, 0x90
LBB0_1153:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_1151:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1153
	jmp	LBB0_1152
	.p2align	4, 0x90
LBB0_117:
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-14, (%r14)
	jmp	LBB0_118
	.p2align	4, 0x90
LBB0_1154:
	addl	$-9, (%r14)
LBB0_118:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1154
	jmp	LBB0_119
	.p2align	4, 0x90
LBB0_1155:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_119:
	addl	$7, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1155
	addl	$-7, (%r14)
	.p2align	4, 0x90
LBB0_121:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_122
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movslq	(%r14), %rax
	movb	$0, (%rbx,%rax)
	addl	$2, (%r14)
	jmp	LBB0_1157
	.p2align	4, 0x90
LBB0_1438:
	addl	$9, (%r14)
LBB0_1157:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1438
	addl	$-9, (%r14)
	jmp	LBB0_1159
	.p2align	4, 0x90
LBB0_1164:
	addl	$-10, (%r14)
LBB0_1159:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_121
	addl	$7, (%r14)
	jmp	LBB0_1161
	.p2align	4, 0x90
LBB0_1439:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$6, (%r14)
LBB0_1161:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1439
	addl	$-6, (%r14)
	jmp	LBB0_1163
	.p2align	4, 0x90
LBB0_1167:
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$3, (%r14)
LBB0_1163:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1164
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-7, (%r14)
	jmp	LBB0_1166
	.p2align	4, 0x90
LBB0_1168:
	addl	$-9, (%r14)
LBB0_1166:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1168
	jmp	LBB0_1167
	.p2align	4, 0x90
LBB0_1169:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_122:
	addl	$7, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1169
	addl	$-7, (%r14)
	jmp	LBB0_124
	.p2align	4, 0x90
LBB0_1176:
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
LBB0_124:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_125
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$2, (%r14)
	jmp	LBB0_1171
	.p2align	4, 0x90
LBB0_1180:
	addl	$8, (%r14)
LBB0_1171:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1172
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	jmp	LBB0_1178
	.p2align	4, 0x90
LBB0_1440:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_1178:
	addl	$4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1440
	jmp	LBB0_1179
	.p2align	4, 0x90
LBB0_1181:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1179:
	addl	$-4, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1181
	jmp	LBB0_1180
	.p2align	4, 0x90
LBB0_1172:
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-7, (%r14)
	jmp	LBB0_1173
	.p2align	4, 0x90
LBB0_1184:
	addl	$-14, (%r14)
LBB0_1173:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1174
	addl	$5, (%r14)
	jmp	LBB0_1183
	.p2align	4, 0x90
LBB0_1185:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
LBB0_1183:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1185
	jmp	LBB0_1184
	.p2align	4, 0x90
LBB0_1174:
	addl	$9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1174
	jmp	LBB0_1175
	.p2align	4, 0x90
LBB0_1189:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1175:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1176
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_1187
	.p2align	4, 0x90
LBB0_1190:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_1191
	.p2align	4, 0x90
LBB0_1441:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$3, (%r14)
LBB0_1191:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1441
	jmp	LBB0_1192
	.p2align	4, 0x90
LBB0_1193:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1192:
	decl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1193
LBB0_1187:
	addl	$7, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1190
	jmp	LBB0_1188
	.p2align	4, 0x90
LBB0_1194:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1188:
	addl	$-6, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1194
	jmp	LBB0_1189
	.p2align	4, 0x90
LBB0_125:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_126
	.p2align	4, 0x90
LBB0_1195:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_126:
	addl	$7, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1195
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-7, (%r14)
	jmp	LBB0_128
	.p2align	4, 0x90
LBB0_129:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	addl	$2, (%r14)
	jmp	LBB0_130
	.p2align	4, 0x90
LBB0_1198:
	addl	$4, (%r14)
LBB0_130:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_131
	addl	$5, (%r14)
	jmp	LBB0_1197
	.p2align	4, 0x90
LBB0_1199:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
LBB0_1197:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1199
	jmp	LBB0_1198
	.p2align	4, 0x90
LBB0_1203:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_131:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_132
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_1201
	.p2align	4, 0x90
LBB0_1204:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_1205
	.p2align	4, 0x90
LBB0_1442:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$3, (%r14)
LBB0_1205:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1442
	jmp	LBB0_1206
	.p2align	4, 0x90
LBB0_1207:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1206:
	decl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1207
LBB0_1201:
	addl	$7, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1204
	jmp	LBB0_1202
	.p2align	4, 0x90
LBB0_1208:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1202:
	addl	$-6, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1208
	jmp	LBB0_1203
	.p2align	4, 0x90
LBB0_132:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	addb	$5, (%rbx,%rax)
	jmp	LBB0_133
	.p2align	4, 0x90
LBB0_1211:
	addl	$9, (%r14)
LBB0_133:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_134
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_1210
	.p2align	4, 0x90
LBB0_1212:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_1210:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1212
	jmp	LBB0_1211
	.p2align	4, 0x90
LBB0_134:
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-5, (%r14)
	jmp	LBB0_135
	.p2align	4, 0x90
LBB0_1213:
	addl	$-9, (%r14)
LBB0_135:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1213
	addl	$9, (%r14)
	jmp	LBB0_137
	.p2align	4, 0x90
LBB0_1224:
	addl	$8, (%r14)
LBB0_137:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1215
	jmp	LBB0_138
	.p2align	4, 0x90
LBB0_1214:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-5, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_1215:
	addl	$5, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1214
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-5, (%r14)
	.p2align	4, 0x90
LBB0_1217:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1218
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	addl	$2, (%r14)
	jmp	LBB0_1226
	.p2align	4, 0x90
LBB0_1443:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$7, (%r14)
LBB0_1226:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1443
	addl	$-7, (%r14)
	jmp	LBB0_1228
	.p2align	4, 0x90
LBB0_1233:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_1228:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1217
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-16, (%r14)
	jmp	LBB0_1230
	.p2align	4, 0x90
LBB0_1444:
	addl	$-9, (%r14)
LBB0_1230:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1444
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_1232
	.p2align	4, 0x90
LBB0_1234:
	addl	$9, (%r14)
LBB0_1232:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1234
	jmp	LBB0_1233
	.p2align	4, 0x90
LBB0_1218:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_1219
	.p2align	4, 0x90
LBB0_1235:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_1219:
	addl	$7, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1235
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-7, (%r14)
	.p2align	4, 0x90
LBB0_1221:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1222
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	addl	$-2, (%r14)
	jmp	LBB0_1237
	.p2align	4, 0x90
LBB0_1445:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$5, (%r14)
LBB0_1237:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1445
	addl	$-5, (%r14)
	jmp	LBB0_1239
	.p2align	4, 0x90
LBB0_1244:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_1239:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1221
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-14, (%r14)
	jmp	LBB0_1241
	.p2align	4, 0x90
LBB0_1446:
	addl	$-9, (%r14)
LBB0_1241:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1446
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$6, (%r14)
	jmp	LBB0_1243
	.p2align	4, 0x90
LBB0_1245:
	addl	$9, (%r14)
LBB0_1243:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1245
	jmp	LBB0_1244
	.p2align	4, 0x90
LBB0_1222:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_1223
	.p2align	4, 0x90
LBB0_1248:
	addl	$-8, (%r14)
LBB0_1223:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1224
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_1247
	.p2align	4, 0x90
LBB0_1249:
	addl	$9, (%r14)
LBB0_1247:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1249
	jmp	LBB0_1248
	.p2align	4, 0x90
LBB0_138:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_138
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	addb	$5, (%rbx,%rax)
	jmp	LBB0_140
	.p2align	4, 0x90
LBB0_1252:
	addl	$9, (%r14)
LBB0_140:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_141
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_1251
	.p2align	4, 0x90
LBB0_1253:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_1251:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1253
	jmp	LBB0_1252
	.p2align	4, 0x90
LBB0_141:
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	addl	$-5, (%r14)
	jmp	LBB0_142
	.p2align	4, 0x90
LBB0_143:
	addl	$-9, (%r14)
LBB0_142:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_143
LBB0_128:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_129
LBB0_35:
	addl	$3, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_63
	movl	(%r14), %eax
	addl	$-4, %eax
	movl	%eax, (%r14)
	cltq
	movzbl	(%rbx,%rax), %edi
	movl	$1, %esi
	callq	*%r15
	addl	$10, (%r14)
	jmp	LBB0_37
	.p2align	4, 0x90
LBB0_1254:
	movl	(%r14), %eax
	addl	$6, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	addl	$3, (%r14)
LBB0_37:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1254
	.p2align	4, 0x90
LBB0_38:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_38
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	addb	$10, (%rbx,%rax)
	jmp	LBB0_40
	.p2align	4, 0x90
LBB0_1257:
	addl	$9, (%r14)
LBB0_40:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_41
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_1256
	.p2align	4, 0x90
LBB0_1258:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_1256:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1258
	jmp	LBB0_1257
	.p2align	4, 0x90
LBB0_41:
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-15, (%r14)
	jmp	LBB0_42
	.p2align	4, 0x90
LBB0_1259:
	addl	$-9, (%r14)
LBB0_42:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1259
	jmp	LBB0_43
	.p2align	4, 0x90
LBB0_1260:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-8, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_43:
	addl	$8, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1260
	addl	$-8, (%r14)
	.p2align	4, 0x90
LBB0_45:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_46
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$8, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movslq	(%r14), %rax
	movb	$0, (%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_1262
	.p2align	4, 0x90
LBB0_1447:
	addl	$9, (%r14)
LBB0_1262:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1447
	addl	$-9, (%r14)
	jmp	LBB0_1264
	.p2align	4, 0x90
LBB0_1269:
	addl	$-10, (%r14)
LBB0_1264:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_45
	addl	$8, (%r14)
	jmp	LBB0_1266
	.p2align	4, 0x90
LBB0_1448:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$7, (%r14)
LBB0_1266:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1448
	addl	$-7, (%r14)
	jmp	LBB0_1268
	.p2align	4, 0x90
LBB0_1272:
	movl	(%r14), %eax
	addl	$8, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$2, (%r14)
LBB0_1268:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1269
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-8, (%r14)
	jmp	LBB0_1271
	.p2align	4, 0x90
LBB0_1273:
	addl	$-9, (%r14)
LBB0_1271:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1273
	jmp	LBB0_1272
	.p2align	4, 0x90
LBB0_1274:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-8, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_46:
	addl	$8, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1274
	addl	$-8, (%r14)
	jmp	LBB0_48
	.p2align	4, 0x90
LBB0_1281:
	movl	(%r14), %eax
	addl	$8, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-5, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-3, (%r14)
LBB0_48:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_49
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$8, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_1276
	.p2align	4, 0x90
LBB0_1285:
	addl	$8, (%r14)
LBB0_1276:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1277
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	jmp	LBB0_1283
	.p2align	4, 0x90
LBB0_1449:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-5, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_1283:
	addl	$5, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1449
	jmp	LBB0_1284
	.p2align	4, 0x90
LBB0_1286:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1284:
	addl	$-5, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1286
	jmp	LBB0_1285
	.p2align	4, 0x90
LBB0_1277:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-8, (%r14)
	jmp	LBB0_1278
	.p2align	4, 0x90
LBB0_1289:
	addl	$-15, (%r14)
LBB0_1278:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1279
	addl	$6, (%r14)
	jmp	LBB0_1288
	.p2align	4, 0x90
LBB0_1290:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
LBB0_1288:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1290
	jmp	LBB0_1289
	.p2align	4, 0x90
LBB0_1279:
	addl	$9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1279
	jmp	LBB0_1280
	.p2align	4, 0x90
LBB0_1294:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1280:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1281
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_1292
	.p2align	4, 0x90
LBB0_1295:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-8, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_1296
	.p2align	4, 0x90
LBB0_1450:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$2, (%r14)
LBB0_1296:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1450
	jmp	LBB0_1297
	.p2align	4, 0x90
LBB0_1298:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1297:
	decl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1298
LBB0_1292:
	addl	$8, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1295
	jmp	LBB0_1293
	.p2align	4, 0x90
LBB0_1299:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1293:
	addl	$-7, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1299
	jmp	LBB0_1294
	.p2align	4, 0x90
LBB0_49:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_50
	.p2align	4, 0x90
LBB0_1300:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-8, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_50:
	addl	$8, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1300
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-8, (%r14)
	jmp	LBB0_52
	.p2align	4, 0x90
LBB0_1301:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$8, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_1302
	.p2align	4, 0x90
LBB0_1318:
	addl	$3, (%r14)
LBB0_1302:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1303
	addl	$6, (%r14)
	jmp	LBB0_1317
	.p2align	4, 0x90
LBB0_1319:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-2, (%r14)
LBB0_1317:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1319
	jmp	LBB0_1318
	.p2align	4, 0x90
LBB0_1323:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1303:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1304
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	jmp	LBB0_1321
	.p2align	4, 0x90
LBB0_1324:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-8, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_1325
	.p2align	4, 0x90
LBB0_1451:
	movl	(%r14), %eax
	decl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-2, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$2, (%r14)
LBB0_1325:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1451
	jmp	LBB0_1326
	.p2align	4, 0x90
LBB0_1327:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1326:
	decl	(%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1327
LBB0_1321:
	addl	$8, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1324
	jmp	LBB0_1322
	.p2align	4, 0x90
LBB0_1328:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$7, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
LBB0_1322:
	addl	$-7, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1328
	jmp	LBB0_1323
	.p2align	4, 0x90
LBB0_1304:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	addb	$5, (%rbx,%rax)
	jmp	LBB0_1305
	.p2align	4, 0x90
LBB0_1331:
	addl	$9, (%r14)
LBB0_1305:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1306
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_1330
	.p2align	4, 0x90
LBB0_1332:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_1330:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1332
	jmp	LBB0_1331
	.p2align	4, 0x90
LBB0_1306:
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$27, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-6, (%r14)
	jmp	LBB0_1307
	.p2align	4, 0x90
LBB0_1333:
	addl	$-9, (%r14)
LBB0_1307:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1333
	addl	$9, (%r14)
	jmp	LBB0_1309
	.p2align	4, 0x90
LBB0_1344:
	addl	$8, (%r14)
LBB0_1309:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1335
	jmp	LBB0_1310
	.p2align	4, 0x90
LBB0_1334:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_1335:
	addl	$6, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1334
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-6, (%r14)
	.p2align	4, 0x90
LBB0_1337:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1338
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$6, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	addl	$2, (%r14)
	jmp	LBB0_1346
	.p2align	4, 0x90
LBB0_1452:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-8, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$8, (%r14)
LBB0_1346:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1452
	addl	$-8, (%r14)
	jmp	LBB0_1348
	.p2align	4, 0x90
LBB0_1353:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_1348:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1337
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$8, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-17, (%r14)
	jmp	LBB0_1350
	.p2align	4, 0x90
LBB0_1453:
	addl	$-9, (%r14)
LBB0_1350:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1453
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$5, (%r14)
	jmp	LBB0_1352
	.p2align	4, 0x90
LBB0_1354:
	addl	$9, (%r14)
LBB0_1352:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1354
	jmp	LBB0_1353
	.p2align	4, 0x90
LBB0_1338:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	jmp	LBB0_1339
	.p2align	4, 0x90
LBB0_1355:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-8, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
LBB0_1339:
	addl	$8, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1355
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$-8, (%r14)
	.p2align	4, 0x90
LBB0_1341:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1342
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$8, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	addl	$-2, (%r14)
	jmp	LBB0_1357
	.p2align	4, 0x90
LBB0_1454:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$-6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$6, (%r14)
LBB0_1357:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1454
	addl	$-6, (%r14)
	jmp	LBB0_1359
	.p2align	4, 0x90
LBB0_1364:
	movl	(%r14), %eax
	incl	%eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	decl	(%r14)
LBB0_1359:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1341
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$6, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-15, (%r14)
	jmp	LBB0_1361
	.p2align	4, 0x90
LBB0_1455:
	addl	$-9, (%r14)
LBB0_1361:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1455
	movl	(%r14), %eax
	addl	$3, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	addl	$6, (%r14)
	jmp	LBB0_1363
	.p2align	4, 0x90
LBB0_1365:
	addl	$9, (%r14)
LBB0_1363:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1365
	jmp	LBB0_1364
	.p2align	4, 0x90
LBB0_1342:
	movslq	(%r14), %rax
	incb	(%rbx,%rax)
	incl	(%r14)
	jmp	LBB0_1343
	.p2align	4, 0x90
LBB0_1368:
	addl	$-8, (%r14)
LBB0_1343:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1344
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	decl	(%r14)
	jmp	LBB0_1367
	.p2align	4, 0x90
LBB0_1369:
	addl	$9, (%r14)
LBB0_1367:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1369
	jmp	LBB0_1368
	.p2align	4, 0x90
LBB0_1310:
	addl	$-9, (%r14)
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1310
	movl	(%r14), %eax
	addl	$4, %eax
	movl	%eax, (%r14)
	cltq
	movb	$0, (%rbx,%rax)
	movl	(%r14), %eax
	addl	$-3, %eax
	movl	%eax, (%r14)
	cltq
	addb	$5, (%rbx,%rax)
	jmp	LBB0_1312
	.p2align	4, 0x90
LBB0_1372:
	addl	$9, (%r14)
LBB0_1312:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	je	LBB0_1313
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	jmp	LBB0_1371
	.p2align	4, 0x90
LBB0_1373:
	movslq	(%r14), %rax
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$9, %eax
	movl	%eax, (%r14)
	cltq
	incb	(%rbx,%rax)
	addl	$-9, (%r14)
LBB0_1371:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1373
	jmp	LBB0_1372
	.p2align	4, 0x90
LBB0_1313:
	movl	(%r14), %eax
	addl	$5, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	movl	(%r14), %eax
	addl	$27, %eax
	movl	%eax, (%r14)
	cltq
	decb	(%rbx,%rax)
	addl	$-6, (%r14)
	jmp	LBB0_1314
	.p2align	4, 0x90
LBB0_1315:
	addl	$-9, (%r14)
LBB0_1314:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1315
LBB0_52:
	movslq	(%r14), %rax
	cmpb	$0, (%rbx,%rax)
	jne	LBB0_1301
	jmp	LBB0_53
LBB0_13:
	xorl	%eax, %eax
	popq	%rbx
	popq	%r14
	popq	%r15
	retq
	.cfi_endproc

.zerofill __DATA,__bss,_ptr,4,2

.subsections_via_symbols
