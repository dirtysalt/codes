package com.dirlt.java.run_crypto;

import org.apache.commons.codec.binary.Base64;

import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.security.SecureRandom;
import java.util.Arrays;

// http://bcllemon.github.io/2015/10/29/2015/python-java-aes/
public class RunCrypto {
    public static int byteArrayToInt(byte[] b) {
        final ByteBuffer bb = ByteBuffer.wrap(b);
        bb.order(ByteOrder.LITTLE_ENDIAN);
        return bb.getInt();
    }

    public static byte[] IntToByteArray(int i) {
        final ByteBuffer bb = ByteBuffer.allocate(Integer.SIZE / Byte.SIZE);
        bb.order(ByteOrder.LITTLE_ENDIAN);
        bb.putInt(i);
        return bb.array();
    }

    public static final String KEY = "1234567890123456";
    public static final SecretKey secretKey = new SecretKeySpec(KEY.getBytes(), "AES");

    public static String encrypt() throws Exception {
        // https://docs.oracle.com/javase/7/docs/api/javax/crypto/Cipher.html
        Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding");
        SecureRandom randomSecureRandom = SecureRandom.getInstance("SHA1PRNG");
        byte[] iv = new byte[cipher.getBlockSize()];
        randomSecureRandom.nextBytes(iv);
        IvParameterSpec iv_spec = new IvParameterSpec(iv);

        String data = "this is plain text";
        int blockSize = cipher.getBlockSize();
        System.out.println("blockSize = " + blockSize + ", dataSize = " + data.length());

        // padding.
        byte[] dataBytes = data.getBytes();
        int plaintextLength = dataBytes.length;
        if (plaintextLength % blockSize != 0) {
            plaintextLength = plaintextLength + (blockSize - (plaintextLength % blockSize));
        }
        byte[] plaintext = new byte[plaintextLength];
        System.arraycopy(dataBytes, 0, plaintext, 0, dataBytes.length);

        cipher.init(Cipher.ENCRYPT_MODE, secretKey, iv_spec);
        byte[] encrypted = cipher.doFinal(plaintext);

        // iv + length + encrypted
        int length = dataBytes.length;
        byte[] length_bytes = IntToByteArray(length);
        byte[] final_bytes = new byte[blockSize + length_bytes.length + encrypted.length];
        int offset = 0;
        System.arraycopy(iv, 0, final_bytes, offset, iv.length);
        offset += iv.length;
        System.arraycopy(length_bytes, 0, final_bytes, offset, length_bytes.length);
        offset += length_bytes.length;
        System.arraycopy(encrypted, 0, final_bytes, offset, encrypted.length);


        byte[] value = Base64.encodeBase64(final_bytes);
        String s = new String(value);
        return s;
    }

    public static String decrypt(String s) throws Exception {
        byte[] value = Base64.decodeBase64(s.getBytes());
        Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding");
        int block_size = cipher.getBlockSize();
        byte[] iv = new byte[block_size];
        byte[] data_size = new byte[4];
        byte[] data = new byte[value.length - block_size - 4];
        int offset = 0;
        System.arraycopy(value, offset, iv, 0, iv.length);
        offset += iv.length;
        System.arraycopy(value, offset, data_size, 0, data_size.length);
        offset += data_size.length;
        System.arraycopy(value, offset, data, 0, data.length);

        IvParameterSpec iv_spec = new IvParameterSpec(iv);
        cipher.init(Cipher.DECRYPT_MODE, secretKey, iv_spec);
        byte[] plain_bytes = cipher.doFinal(data);
        int plain_size = byteArrayToInt(data_size);
        byte[] final_plain_bytes = Arrays.copyOfRange(plain_bytes, 0, plain_size);
        System.out.println("plain size = " + plain_size);
        String plain_text = new String(final_plain_bytes);
        return plain_text;
    }

    public static void main(String args[]) throws Exception {
        String s = encrypt();
        System.out.println(s);
        String s2 = decrypt(s);
        System.out.println(s2);
    }
}
